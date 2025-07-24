# AI Document Summarizer (Gemini-Powered)

Summarize PDF, DOCX, or TXT files using Google Gemini (Generative AI) models. Upload a document and get a concise summary instantly!

## Features
- Upload PDF, DOCX, or TXT files
- Extracts and summarizes text using Gemini
- Responsive, modern UI with dark/light mode
- Animated, beautiful background

## Tech Stack
- **Frontend:** React (Vite), CSS
- **Backend:** FastAPI (Python)
- **AI:** Google Gemini (Generative AI)
- **File Extraction:** pdfplumber, python-docx

---

## Setup Instructions

### 1. Clone the Repository
```sh
# Clone and enter the project directory
cd path/to/your/project
```

### 2. Backend Setup
```sh
cd backend
pip install -r requirements.txt
```

#### Configure Gemini API Key
- Create a file named `.env` in the `backend` folder:
  ```
  GOOGLE_API_KEY=your_gemini_api_key_here
  ```
- **Note:** The variable name must be `GOOGLE_API_KEY` (no quotes, no spaces).

#### Start the Backend
```sh
uvicorn main:app --reload
```
- The backend will run at [http://localhost:8000](http://localhost:8000)

### 3. Frontend Setup
```sh
cd ../frontend
npm install
npm run dev
```
- The frontend will run at [http://localhost:5173](http://localhost:5173)

---

## Usage
1. Open [http://localhost:5173](http://localhost:5173) in your browser.
2. Upload a PDF, DOCX, or TXT file.
3. Wait for the summary to appear below the upload box.
4. Use the dark/light mode toggle as desired.

---

## Troubleshooting
- **Gemini API key not found:**
  - Ensure `.env` is in the `backend` folder and named correctly.
  - The variable must be `GOOGLE_API_KEY`.
  - Restart the backend after editing `.env`.
- **No text found in document:**
  - The PDF may be scanned (image-only). Try a different file or add OCR support.
- **Other errors:**
  - Check your backend terminal for error messages and share them for help.

---

## Security
- Never share your API key publicly or commit it to version control.
- Use environment variables for all secrets.

---

## License
MIT
