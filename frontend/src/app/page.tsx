import UploadForm from "../components/UploadForm";

export default function Page() {
  return (
    <main style={{ padding: 24 }}>
      <h1>Department Sales Aggregator</h1>
      <p>Upload a large CSV. We’ll aggregate sales by department and give you a result file.</p>
      <UploadForm />
    </main>
  );
}
