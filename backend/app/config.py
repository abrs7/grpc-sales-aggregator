from __future__ import annotations
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
STORAGE_DIR = (BASE_DIR / "storage").resolve()
UPLOADS_DIR = STORAGE_DIR / "uploads"
RESULTS_DIR = STORAGE_DIR / "results"

GRPC_HOST = os.getenv("GRPC_HOST", "0.0.0.0")
GRPC_PORT = int(os.getenv("GRPC_PORT", "50051"))

# Simple static HTTP server to serve result files
HTTP_HOST = os.getenv("HTTP_HOST", "0.0.0.0")
HTTP_PORT = int(os.getenv("HTTP_PORT", "8080"))

# Create dirs at import-time
for d in (STORAGE_DIR, UPLOADS_DIR, RESULTS_DIR):
    d.mkdir(parents=True, exist_ok=True)
