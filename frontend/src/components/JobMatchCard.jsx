function JobMatchCard({ jobMatch }) {
  return (
    <div className="card">
      <h2>Job Match</h2>

      <h3>Match Score: {jobMatch.match_score}%</h3>

      <p>
        <strong>Matched Skills:</strong>{" "}
        {jobMatch.matched_skills.join(", ") || "None"}
      </p>

      <p>
        <strong>Missing Skills:</strong>{" "}
        {jobMatch.missing_skills.join(", ") || "None"}
      </p>

      <p>
        <strong>Extra Skills:</strong>{" "}
        {jobMatch.extra_skills.join(", ") || "None"}
      </p>
    </div>
  );
}

export default JobMatchCard;