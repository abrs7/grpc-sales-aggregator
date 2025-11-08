from __future__ import annotations
import grpc
from concurrent import futures
import threading
from pathlib import Path
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os, sys
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from .config import GRPC_HOST, GRPC_PORT, HTTP_HOST, HTTP_PORT, STORAGE_DIR, RESULTS_DIR
from backend.generated import sales_pb2_grpc
from .services.sales_service import SalesService

def serve_static_results():
    """
    Serve ./storage/results as /results/* over HTTP (for simple downloadable links).
    This avoids using any web framework.
    """
    class Handler(SimpleHTTPRequestHandler):
        def translate_path(self, path):
            # Map /results/<file> -> RESULTS_DIR/<file>
            if path.startswith("/results/"):
                fname = path.split("/results/", 1)[1]
                return str(RESULTS_DIR / fname)
            # fallback to storage root
            return str((STORAGE_DIR / path.lstrip("/")).resolve())

    # Avoid address already in use on quick restarts
    TCPServer.allow_reuse_address = True
    with TCPServer((HTTP_HOST, HTTP_PORT), Handler) as httpd:
        print(f"[HTTP] Serving results from {RESULTS_DIR} at http://{HTTP_HOST}:{HTTP_PORT}/results/<file>")
        httpd.serve_forever()

def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    sales_pb2_grpc.add_SalesServiceServicer_to_server(SalesService(), server)
    server.add_insecure_port(f"{GRPC_HOST}:{GRPC_PORT}")
    print(f"[gRPC] Listening on {GRPC_HOST}:{GRPC_PORT}")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    # Run HTTP static server in a background thread
    t = threading.Thread(target=serve_static_results, daemon=True)
    t.start()
    # Run gRPC server (blocking)
    serve_grpc()
