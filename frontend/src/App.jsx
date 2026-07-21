import "./App.css";
import { useState } from "react";
import axios from "axios";
import ScoreCard from "./components/ScoreCard";
import SkillsCard from "./components/SkillsCard";
import StrengthCard from "./components/StrengthCard";
import ProjectCard from "./components/ProjectCard";
import EducationCard from "./components/EducationCard";
import JobMatchCard from "./components/JobMatchCard";





function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    setLoading(true);
  console.log("Button clicked!");

  if (!file) {
    alert("Please select a resume.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);
  formData.append("job_description", jobDescription);

  console.log(formData.get("file"));
  console.log(formData.get("job_description"));

  try {
    
    const response = await axios.post(
      "http://127.0.0.1:8000/upload",
      formData
    );

    console.log(response.data);
  
    setResult(response.data);

  } catch (err) {
    console.error(err);

    if (err.response) {
      console.log(err.response.data);
      alert(JSON.stringify(err.response.data));
    } else {
      alert(err.message);
    }
  }
  finally {
    setLoading(false);
  }  
};

  return (
    <div className="container">
      <h1>ResumeFit</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <textarea
        placeholder="Paste the Job Description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        rows={8}
      />

      <button
        onClick={handleUpload}
        disabled={loading}
      >
        {loading ? "Analyzing Resume..." : "Analyze Resume"}
      </button>

      {result && (
        <>
          <ScoreCard score={result.analysis.overall_score} />
          
          <JobMatchCard jobMatch={result.job_match} />
          <SkillsCard skills={result.resume_data.skills} />
          <StrengthCard analysis={result.analysis} />
          <ProjectCard projects={result.resume_data.projects} />
          <EducationCard education={result.resume_data.education} />
        </>
      )}
    </div>
  );
}

export default App;