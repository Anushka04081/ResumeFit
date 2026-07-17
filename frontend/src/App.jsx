import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a resume.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert("Upload failed.");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>ResumeFit</h1>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={handleUpload}>
        Analyze Resume
      </button>

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>Analysis Result</h2>

          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;