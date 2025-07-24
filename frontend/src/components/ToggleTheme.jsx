import React, { useEffect, useState } from "react";

function ToggleTheme() {
  const [dark, setDark] = useState(() => window.matchMedia("(prefers-color-scheme: dark)").matches);

  useEffect(() => {
    document.body.className = dark ? "dark" : "";
  }, [dark]);

  return (
    <button onClick={() => setDark((d) => !d)}>
      {dark ? "🌙 Dark" : "☀️ Light"}
    </button>
  );
}

export default ToggleTheme;
