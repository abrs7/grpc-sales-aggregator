from __future__ import annotations
import uuid
from pathlib import Path
from ..config import UPLOADS_DIR, RESULTS_DIR, HTTP_PORT

def new_upload_path() -> Path:
    return UPLOADS_DIR / f"upload_{uuid.uuid4().hex}.csv"

def new_result_path() -> Path:
    return RESULTS_DIR / f"result_{uuid.uuid4().hex}.csv"

def make_download_url(filename: str) -> str:
    # Downloads are served from /results/<filename> by the built-in file server
    return f"http://localhost:{HTTP_PORT}/results/{filename}"
