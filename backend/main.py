from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils import extract_text_from_file, chunk_text
import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE_MB = 10
HF_SUMMARIZATION_MODEL = "facebook/bart-large-cnn"
HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_SUMMARIZATION_MODEL}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

def summarize_with_hf(text):
    response = requests.post(
        HF_API_URL,
        headers=HEADERS,
        json={"inputs": text, "parameters": {"max_length": 300, "min_length": 30, "do_sample": False}},
        timeout=60
    )
    if response.status_code != 200:
        raise Exception(f"Hugging Face API error: {response.status_code} {response.text}")
    result = response.json()
    # The result is usually a list of dicts with 'summary_text'
    if isinstance(result, list) and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        return str(result)

@app.post("/summarize/")
async def summarize(file: UploadFile = File(...)):
    if file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain"
    ]:
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large.")
    try:
        text = extract_text_from_file(file.filename, contents)
        if not text.strip():
            raise HTTPException(status_code=400, detail="No text found in document.")

        # Chunking for large docs
        chunks = chunk_text(text, max_tokens=900)  # BART can handle ~1024 tokens
        summaries = []
        for chunk in chunks:
            summary = summarize_with_hf(chunk)
            summaries.append(summary.strip())
        summary = "\n\n".join(summaries)
        return JSONResponse({"original": text, "summary": summary})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hugging Face API error: {str(e)}")
