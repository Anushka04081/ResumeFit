import "../styles/ScoreCard.css";

function ScoreCard({ score }) {
  return (
    <div className="score-card">
      <h2>Resume Score</h2>

      <div className="score-circle">
        {score}%
      </div>
    </div>
  );
}

export default ScoreCard;