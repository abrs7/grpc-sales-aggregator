from __future__ import annotations
import sys
from pathlib import Path
import grpc

from ..config import RESULTS_DIR
from ..core.file_manager import new_upload_path, new_result_path, make_download_url
from ..core.aggregator import aggregate_sales_from_csv

# Ensure backend directory is on sys.path
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from backend.generated import sales_pb2, sales_pb2_grpc


class SalesService(sales_pb2_grpc.SalesServiceServicer):
    def UploadCSV(self, request: sales_pb2.UploadRequest, context: grpc.ServicerContext):
        """Handles unary UploadCSV request: receives one file blob, processes CSV."""
        upload_path = new_upload_path()
        result_path = new_result_path()

        # Save uploaded CSV data to a temp file
        with upload_path.open("wb") as f:
            f.write(request.data)

        # Process the CSV file (streaming read, low memory)
        metrics = aggregate_sales_from_csv(upload_path, result_path)

        result_filename = result_path.name
        download_url = make_download_url(result_filename)

        # Send response metadata
        return sales_pb2.UploadResponse(
            result_id=result_filename,
            download_url=download_url,
            rows=metrics.rows,
            bad_rows=metrics.bad_rows,
            departments=metrics.departments,
            elapsed_sec=metrics.elapsed_sec,
        )

    def DownloadResult(self, request: sales_pb2.DownloadRequest, context: grpc.ServicerContext):
        """Returns a CSV file via gRPC (optional alternative to HTTP)."""
        filename = request.result_id
        target = RESULTS_DIR / filename
        if not target.exists():
            context.abort(grpc.StatusCode.NOT_FOUND, "Result file not found")

        data = target.read_bytes()
        return sales_pb2.DownloadResponse(data=data)
