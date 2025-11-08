# backend/Dockerfile
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependencies first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend source code into /app/backend
COPY . /app/backend

# Create __init__.py files to make Python recognize these as packages
RUN touch /app/backend/__init__.py && \
    touch /app/backend/generated/__init__.py && \
    touch /app/backend/app/__init__.py

# Generate Python gRPC stubs
RUN python -m grpc_tools.protoc -I=/app/backend/proto \
    --python_out=/app/backend/generated \
    --grpc_python_out=/app/backend/generated \
    /app/backend/proto/sales.proto

# Fix the import in the generated _grpc.py file
# The generated file imports 'sales_pb2' but needs to import from the same package
RUN sed -i 's/^import sales_pb2 as sales__pb2$/from . import sales_pb2 as sales__pb2/g' /app/backend/generated/sales_pb2_grpc.py

# Set PYTHONPATH so Python can find the backend module
ENV PYTHONPATH=/app:$PYTHONPATH

# Expose gRPC (50051) and HTTP (8080) ports
EXPOSE 50051 8080

# Default command to run the gRPC + HTTP server
CMD ["python", "-m", "backend.app.main"]