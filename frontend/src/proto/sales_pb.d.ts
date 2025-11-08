import * as jspb from 'google-protobuf'



export class UploadChunk extends jspb.Message {
  getData(): Uint8Array | string;
  getData_asU8(): Uint8Array;
  getData_asB64(): string;
  setData(value: Uint8Array | string): UploadChunk;

  getFilename(): string;
  setFilename(value: string): UploadChunk;

  getEof(): boolean;
  setEof(value: boolean): UploadChunk;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UploadChunk.AsObject;
  static toObject(includeInstance: boolean, msg: UploadChunk): UploadChunk.AsObject;
  static serializeBinaryToWriter(message: UploadChunk, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UploadChunk;
  static deserializeBinaryFromReader(message: UploadChunk, reader: jspb.BinaryReader): UploadChunk;
}

export namespace UploadChunk {
  export type AsObject = {
    data: Uint8Array | string,
    filename: string,
    eof: boolean,
  }
}

export class UploadRequest extends jspb.Message {
  getData(): Uint8Array | string;
  getData_asU8(): Uint8Array;
  getData_asB64(): string;
  setData(value: Uint8Array | string): UploadRequest;

  getFilename(): string;
  setFilename(value: string): UploadRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UploadRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UploadRequest): UploadRequest.AsObject;
  static serializeBinaryToWriter(message: UploadRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UploadRequest;
  static deserializeBinaryFromReader(message: UploadRequest, reader: jspb.BinaryReader): UploadRequest;
}

export namespace UploadRequest {
  export type AsObject = {
    data: Uint8Array | string,
    filename: string,
  }
}

export class UploadResponse extends jspb.Message {
  getResultId(): string;
  setResultId(value: string): UploadResponse;

  getDownloadUrl(): string;
  setDownloadUrl(value: string): UploadResponse;

  getRows(): number;
  setRows(value: number): UploadResponse;

  getBadRows(): number;
  setBadRows(value: number): UploadResponse;

  getDepartments(): number;
  setDepartments(value: number): UploadResponse;

  getElapsedSec(): number;
  setElapsedSec(value: number): UploadResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UploadResponse.AsObject;
  static toObject(includeInstance: boolean, msg: UploadResponse): UploadResponse.AsObject;
  static serializeBinaryToWriter(message: UploadResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UploadResponse;
  static deserializeBinaryFromReader(message: UploadResponse, reader: jspb.BinaryReader): UploadResponse;
}

export namespace UploadResponse {
  export type AsObject = {
    resultId: string,
    downloadUrl: string,
    rows: number,
    badRows: number,
    departments: number,
    elapsedSec: number,
  }
}

export class DownloadRequest extends jspb.Message {
  getResultId(): string;
  setResultId(value: string): DownloadRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DownloadRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DownloadRequest): DownloadRequest.AsObject;
  static serializeBinaryToWriter(message: DownloadRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DownloadRequest;
  static deserializeBinaryFromReader(message: DownloadRequest, reader: jspb.BinaryReader): DownloadRequest;
}

export namespace DownloadRequest {
  export type AsObject = {
    resultId: string,
  }
}

export class DownloadResponse extends jspb.Message {
  getData(): Uint8Array | string;
  getData_asU8(): Uint8Array;
  getData_asB64(): string;
  setData(value: Uint8Array | string): DownloadResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DownloadResponse.AsObject;
  static toObject(includeInstance: boolean, msg: DownloadResponse): DownloadResponse.AsObject;
  static serializeBinaryToWriter(message: DownloadResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DownloadResponse;
  static deserializeBinaryFromReader(message: DownloadResponse, reader: jspb.BinaryReader): DownloadResponse;
}

export namespace DownloadResponse {
  export type AsObject = {
    data: Uint8Array | string,
  }
}

