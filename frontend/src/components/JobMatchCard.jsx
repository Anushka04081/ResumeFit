import "../styles/JobMatchCard.css";

function JobMatchCard({ jobMatch }) {
  return (
    <div className="job-card">
      <h2>🎯 Job Match Analysis</h2>

      <div className="match-score">
        {jobMatch.match_score}%
      </div>

      <div className="skill-section">
        <h3>✅ Matched Skills</h3>

        <div className="badge-container">
          {jobMatch.matched_skills.length ? (
            jobMatch.matched_skills.map((skill, index) => (
              <span key={index} className="badge matched">
                {skill}
              </span>
            ))
          ) : (
            <p>None</p>
          )}
        </div>
      </div>

      <div className="skill-section">
        <h3>❌ Missing Skills</h3>

        <div className="badge-container">
          {jobMatch.missing_skills.length ? (
            jobMatch.missing_skills.map((skill, index) => (
              <span key={index} className="badge missing">
                {skill}
              </span>
            ))
          ) : (
            <p>None</p>
          )}
        </div>
      </div>

      <div className="skill-section">
        <h3>💡 Extra Skills</h3>

        <div className="badge-container">
          {jobMatch.extra_skills.length ? (
            jobMatch.extra_skills.map((skill, index) => (
              <span key={index} className="badge extra">
                {skill}
              </span>
            ))
          ) : (
            <p>None</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default JobMatchCard;