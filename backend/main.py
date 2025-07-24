from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils import extract_text_from_file, chunk_text
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
print("GOOGLE_API_KEY from .env:", os.getenv("GOOGLE_API_KEY"))  # This should print your key (or at least the first few characters)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE_MB = 10

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
        chunks = chunk_text(text, max_tokens=3000)
        summaries = []
        model = genai.GenerativeModel("gemini-pro")
        for chunk in chunks:
            prompt = f"Summarize the following text:\n\n{chunk}\n\nSummary:"
            response = model.generate_content(prompt)
            summary = response.text.strip() if hasattr(response, 'text') else str(response)
            summaries.append(summary)
        summary = "\n\n".join(summaries)
        return JSONResponse({"original": text, "summary": summary})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini API error: {str(e)}")
