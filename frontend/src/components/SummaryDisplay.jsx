import React from "react";

function SummaryDisplay({ original, summary }) {
  if (!original && !summary) return null;
  return (
    <div className="summary-container">
      <h2>Original Text</h2>
      <pre className="original">{original}</pre>
      <h2>Summary</h2>
      <pre className="summary">{summary}</pre>
    </div>
  );
}

export default SummaryDisplay;
