import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import SummaryDisplay from "./components/SummaryDisplay";
import ToggleTheme from "./components/ToggleTheme";
import "./styles/main.css";

function App() {
  const [original, setOriginal] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  return (
    <div className="app-bg-wrapper">
      {/* Ghibli-style SVGs */}
      <div className="ghibli-bg">
        {/* Soft clouds */}
        <svg className="cloud cloud1" viewBox="0 0 200 60" fill="none">
          <ellipse cx="50" cy="30" rx="50" ry="30" fill="#fff" fillOpacity="0.7"/>
          <ellipse cx="120" cy="35" rx="40" ry="25" fill="#fff" fillOpacity="0.5"/>
          <ellipse cx="170" cy="30" rx="30" ry="18" fill="#fff" fillOpacity="0.4"/>
        </svg>
        <svg className="cloud cloud2" viewBox="0 0 120 40" fill="none">
          <ellipse cx="40" cy="20" rx="40" ry="20" fill="#fff" fillOpacity="0.6"/>
          <ellipse cx="90" cy="22" rx="30" ry="14" fill="#fff" fillOpacity="0.4"/>
        </svg>
        {/* Soft hill */}
        <svg className="hill" viewBox="0 0 400 120" fill="none">
          <path d="M0 100 Q100 20 200 100 T400 100 V120 H0 Z" fill="#a7f3d0" fillOpacity="0.5"/>
        </svg>
      </div>
      {/* Blurred colorful blobs */}
      <div className="bg-blobs">
        <span className="blob blob1"></span>
        <span className="blob blob2"></span>
        <span className="blob blob3"></span>
      </div>
      {/* Animated background icons */}
      <div className="animated-bg-icons">
        {/* Icons removed as requested */}
      </div>
      {/* Main content */}
      <div className="container">
        <ToggleTheme />
        <h1>AI Document Summarizer</h1>
        <FileUpload setOriginal={setOriginal} setSummary={setSummary} setLoading={setLoading} />
        {loading && <p>Summarizing...</p>}
        <SummaryDisplay original={original} summary={summary} />
      </div>
    </div>
  );
}

export default App;
