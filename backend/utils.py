import pdfplumber
import docx
import io
import re

def extract_text_from_file(filename, file_bytes):
    if filename.endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif filename.endswith(".docx"):
        doc = docx.Document(io.BytesIO(file_bytes))
        return "\n".join([para.text for para in doc.paragraphs])
    elif filename.endswith(".txt"):
        return file_bytes.decode("utf-8", errors="ignore")
    else:
        return ""

def chunk_text(text, max_tokens=3000):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks, chunk, length = [], "", 0
    for sent in sentences:
        if length + len(sent) > max_tokens * 4:
            chunks.append(chunk)
            chunk, length = "", 0
        chunk += sent + " "
        length += len(sent)
    if chunk:
        chunks.append(chunk)
    return chunks
