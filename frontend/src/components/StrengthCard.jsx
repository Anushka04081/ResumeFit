import "../styles/StrengthCard.css";

function StrengthCard({ analysis }) {
  return (
    <div className="strength-card">
      <div className="card-section">
        <h2>✅ Strengths</h2>

        <ul>
          {analysis.strengths.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>

      <div className="card-section">
        <h2>⚠️ Improvements</h2>

        <ul>
          {analysis.improvements.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>

      <div className="card-section">
        <h2>📌 Missing Sections</h2>

        <ul>
          {analysis.missing_sections.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default StrengthCard;
