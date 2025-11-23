import React, { useState, useEffect, useRef } from "react";
import { digest, hmac } from "./crypto.js";

const algorithms = [
  "SHA-1","SHA-224","SHA-256","SHA-384","SHA-512",
  "BLAKE2B","BLAKE2S"
];

export default function App() {
  const [text, setText] = useState("NOVAK Protocol Integrity Engine");
  const [intervalMs, setIntervalMs] = useState(1000);
  const [live, setLive] = useState(true);
  const [secret, setSecret] = useState("");
  const [format, setFormat] = useState("hex");
  const [history, setHistory] = useState([]);
  const fileRef = useRef(null);

  useEffect(() => {
    if (!live) return;
    const timer = setInterval(update, intervalMs);
    return () => clearInterval(timer);
  }, [text, secret, intervalMs, live]);

  async function update() {
    const results = {};
    for (const algo of algorithms) {
      results[algo] = secret
        ? await hmac(algo.replace("BLAKE","SHA"), secret, text)
        : await digest(algo, text);
    }
    setHistory(h => [...h.slice(-49), { time: Date.now(), results }]);
  }

  function copy(val) {
    navigator.clipboard.writeText(val);
  }

  function exportJSON() {
    const blob = new Blob([JSON.stringify(history, null, 2)], { type: "application/json" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "novak-hash-history.json";
    link.click();
  }

  function onFile(e) {
    const reader = new FileReader();
    reader.onload = r => setText(r.target.result);
    reader.readAsText(e.target.files[0]);
  }

  return (
    <div style={{ padding: 20, fontFamily: "Arial", color: "white", background: "#0d1117", minHeight: "100vh" }}>

      <h1>NOVAK Live Integrity Workbench</h1>

      <textarea
        value={text}
        onChange={e => setText(e.target.value)}
        style={{ width: "100%", height: 150, background: "#161b22", color: "white", padding: 10 }}
      />

      <div style={{ marginTop: 10 }}>
        <label>Interval (ms): </label>
        <input type="number" value={intervalMs} min="50" step="50" onChange={e => setIntervalMs(+e.target.value)} />

        <label style={{ marginLeft: 20 }}>Live: </label>
        <select value={live ? "on" : "off"} onChange={e => setLive(e.target.value === "on")}>
          <option value="on">On</option>
          <option value="off">Off</option>
        </select>

        <label style={{ marginLeft: 20 }}>HMAC Secret: </label>
        <input type="text" value={secret} onChange={e => setSecret(e.target.value)} />
      </div>

      <button onClick={() => fileRef.current.click()} style={{ marginTop: 10 }}>Upload File</button>
      <input ref={fileRef} type="file" style={{ display: "none" }} onChange={onFile} />

      <h2>Hashes</h2>
      {history[history.length - 1] &&
        algorithms.map(a => {
          const value = history[history.length - 1].results[a];
          return (
            <div key={a} style={{ background: "#161b22", padding: 10, marginBottom: 6 }}>
              <b>{a}:</b> {value}
              <button style={{ marginLeft: 10 }} onClick={() => copy(value)}>Copy</button>
            </div>
          );
        })
      }

      <button onClick={exportJSON} style={{ marginTop: 15 }}>Export JSON History</button>

      <h2>Timeline (Last 50)</h2>
      <ul>
        {history.map((h, i) => (
          <li key={i}>{new Date(h.time).toLocaleTimeString()}</li>
        ))}
      </ul>
    </div>
  );
}
