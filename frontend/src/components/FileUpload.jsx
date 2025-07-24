import React from "react";
import axios from "axios";

function FileUpload({ setOriginal, setSummary, setLoading }) {
  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setLoading(true);
    setOriginal("");
    setSummary("");
    const formData = new FormData();
    formData.append("file", file);
    try {
      const res = await axios.post("http://localhost:8000/summarize/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setOriginal(res.data.original);
      setSummary(res.data.summary);
    } catch (err) {
      alert(err.response?.data?.detail || "Error summarizing document.");
    }
    setLoading(false);
  };

  return (
    <div>
      <input type="file" accept=".pdf,.docx,.txt" onChange={handleFileChange} />
    </div>
  );
}

export default FileUpload;
