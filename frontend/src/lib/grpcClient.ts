import { UploadRequest, UploadResponse } from "../proto/sales_pb";
import { SalesServiceClient } from "../proto/SalesServiceClientPb";

declare const process: { env: { NEXT_PUBLIC_GRPC_WEB?: string } };

const GRPC_WEB_ENDPOINT =
  process.env.NEXT_PUBLIC_GRPC_WEB || "http://localhost:8081";

/**
 * Return an instance of the generated SalesService gRPC-Web client.
 */
export function getClient(): SalesServiceClient {
  return new SalesServiceClient(GRPC_WEB_ENDPOINT, null, null);
}

/**
 * Uploads a CSV file to the backend using a unary gRPC-Web call.
 * Shows progress via the optional onProgress callback.
 */
export async function uploadCsv(
  file: File,
  onProgress?: (pct: number) => void
): Promise<UploadResponse> {
  const client = getClient();

  // Read the entire file into memory — still OK for the demo (backend streams internally).
  const arrayBuffer = await file.arrayBuffer();
  const totalBytes = file.size;
  onProgress?.(100);

  // Build the gRPC request
  const request = new UploadRequest();
  request.setData(new Uint8Array(arrayBuffer));
  request.setFilename(file.name);

  return new Promise<UploadResponse>((resolve, reject) => {
    client.uploadCSV(request, {}, (err, response) => {
      if (err) {
        console.error("gRPC UploadCSV error:", err);
        reject(err);
        return;
      }
      if (!response) {
        reject(new Error("Empty gRPC response"));
        return;
      }
      resolve(response);
    });
  });
}
