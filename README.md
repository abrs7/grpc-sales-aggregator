# 📦 gRPC Sales Aggregator

A lightweight backend service built in **pure Python + gRPC** (no web frameworks) that processes large CSV files by aggregating departmental sales data.  
The system includes a **Next.js frontend** for file uploads and an **Envoy proxy** for gRPC-Web compatibility.

---

## 🚀 Features

- **Pure Python backend** using `grpcio` (no Django/FastAPI/Flask)
- **Unary UploadCSV** RPC with file upload and streaming CSV processing (low memory)
- **Envoy proxy** for browser compatibility (gRPC-Web → gRPC)
- **Next.js frontend** with file upload UI and download link
- **Memory-efficient** CSV aggregation (streamed I/O)
- **Dockerized** for quick setup (backend + envoy + frontend)
- **Unit tests** for aggregation logic

---

## 🧱 Architecture Overview

```
Browser (Next.js)
       ↓  gRPC-Web
[ Envoy Proxy :8081 ]
       ↓  HTTP/2 gRPC
[ Python gRPC Server :50051 ]
       ↳ Processes CSVs line-by-line
       ↳ Stores results under /storage/results
       ↳ Serves files via :8080 HTTP
```

---

## 🗂️ Project Structure

```
grpc_sales_aggregator/
├── backend/
│   ├── app/
│   │   ├── main.py                 # gRPC + HTTP servers
│   │   ├── services/sales_service.py
│   │   ├── core/aggregator.py      # CSV processing logic
│   │   ├── core/file_manager.py    # File paths, UUIDs
│   │   └── config.py
│   ├── generated/                  # Auto-generated protobuf stubs
│   ├── proto/sales.proto           # gRPC interface
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_aggregator.py
│
├── envoy/
│   ├── envoy.yaml                  # gRPC-Web proxy config
│   └── Dockerfile
│
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── src/app/page.tsx
│   ├── src/components/UploadForm.tsx
│   └── src/lib/grpcClient.ts
│
├── docker-compose.yml
└── README.md
```

---

## 🧩 Protobuf Definition

`backend/proto/sales.proto`
```proto
syntax = "proto3";

package sales.v1;

service SalesService {
  rpc UploadCSV (UploadRequest) returns (UploadResponse);
  rpc DownloadResult (DownloadRequest) returns (DownloadResponse);
}

message UploadRequest {
  bytes data = 1;
  string filename = 2;
}

message UploadResponse {
  string result_id = 1;
  string download_url = 2;
  uint64 rows = 3;
  uint64 bad_rows = 4;
  uint64 departments = 5;
  double elapsed_sec = 6;
}

message DownloadRequest {
  string result_id = 1;
}

message DownloadResponse {
  bytes data = 1;
}
```

---

## 🧰 Requirements

- Python 3.11+
- Node.js 20+
- Docker + Docker Compose
- protoc (Protocol Buffers compiler)
- gRPC-Web plugin (for frontend stub generation)

---

## ⚙️ Setup

### 1️⃣ Clone and enter the project
```bash
git clone https://github.com/abrs7/grpc-sales-aggregator.git
cd grpc-sales-aggregator
```

### 2️⃣ Generate gRPC stubs

#### Backend:
```bash
python -m grpc_tools.protoc -I=backend/proto   --python_out=backend/generated   --grpc_python_out=backend/generated   backend/proto/sales.proto
```

#### Frontend:
```bash
cd frontend
npm install
npm run proto
```

---

## 🐳 Run with Docker

From the **project root**:
```bash
docker compose up --build
```

Wait until you see:
```
[gRPC] Listening on 0.0.0.0:50051
[HTTP] Serving results from .../storage/results
```

Then open:
👉 [http://localhost:3000](http://localhost:3000)

---

## 🖥️ Ports

| Service | Port | Description |
|----------|------|-------------|
| Frontend (Next.js) | **3000** | Web UI |
| Envoy Proxy | **8081** | gRPC-Web endpoint |
| gRPC Backend | **50051** | Python gRPC service |
| HTTP File Server | **8080** | Result CSV downloads |

---

## 🧪 Testing (Backend)

Run local tests:

```bash
cd backend
pytest -q
```

Sample test in `tests/test_aggregator.py` validates CSV aggregation output.

---

## 🧠 Algorithm & Complexity

The backend uses **streaming I/O** to process arbitrarily large CSVs without loading them fully into memory.

| Operation | Complexity |
|------------|-------------|
| Time | **O(n)** — each row processed once |
| Memory | **O(d)** — where *d* = number of unique departments |

---

## 🔒 Security Notes

- No authentication is enabled (for demo/test simplicity)
- Production deployments should add:
  - Auth tokens or mTLS for gRPC
  - Signed download URLs (for result files)
  - Rate limiting on upload endpoints

---

## 🧰 Useful Commands

### Rebuild everything cleanly
```bash
docker compose build --no-cache
docker compose up
```

### View logs
```bash
docker compose logs -f backend
```

### Stop all containers
```bash
docker compose down
```

---

## ✅ Deliverables Summary

| Deliverable | Status |
|--------------|--------|
| Python gRPC backend | ✅ |
| CSV streaming processor | ✅ |
| Frontend gRPC-Web upload UI | ✅ |
| Envoy proxy for gRPC-Web | ✅ |
| Unit tests (Pytest) | ✅ |
| Dockerized setup | ✅ |
| README + documentation | ✅ |

---

## 🧑‍💻 Author
**Abraham Asrat**  
📧 [abrahamasrat791@gmail.com](mailto:abrahamasrat791@gmail.com)  
💼 [LinkedIn / GitHub profile link]