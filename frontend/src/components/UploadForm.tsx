"use client";

import React, { useState } from "react";
import { uploadCsv } from "../lib/grpcClient";

export default function UploadForm() {
  const [file, setFile] = useState(null as File | null);
  const [progress, setProgress] = useState<number>(0);
  const [resultUrl, setResultUrl] = useState("");

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return;
    setProgress(0);
    setResultUrl("");
    try {
      const resp = await uploadCsv(file, setProgress);
      setResultUrl(resp.getDownloadUrl());
    } catch (err: any) {
      alert(err.message || "Upload failed");
    }
  };

  return (
    <form onSubmit={onSubmit} style={{ display: "grid", gap: 12, maxWidth: 480 }}>
      <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files?.[0] ?? null)} />
      <progress max={100} value={progress} />
      <button type="submit" disabled={!file}>Upload & Process</button>
      {resultUrl && (
        <a href={resultUrl} target="_blank" rel="noreferrer">Download Result CSV</a>
      )}
    </form>
  );
}
