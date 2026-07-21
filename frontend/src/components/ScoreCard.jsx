import "../styles/ScoreCard.css";

function ScoreCard({ score }) {
  return (
    <div className="score-card">

      <h2>Resume Score</h2>

      <div className="score-circle">
        <span>{score}</span>
        <small>/100</small>
      </div>

      <p className="score-text">
        {score >= 80
          ? "Excellent Resume!"
          : score >= 60
          ? "Good Resume"
          : "Needs Improvement"}
      </p>

    </div>
  );
}

export default ScoreCard;