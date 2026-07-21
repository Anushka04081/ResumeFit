import "../styles/SkillsCard.css";

function SkillsCard({ skills }) {
  return (
    <div className="skills-card">
      <h2>🛠 Technical Skills</h2>

      {skills.map((skill, index) => (
        <div key={index} className="skill-row">

          <div className="skill-name">
            {skill.name}
          </div>

          <div
            className={
              skill.implemented
                ? "implemented"
                : "not-implemented"
            }
          >
            {skill.implemented
              ? "✅ Implemented"
              : "🟡 Mentioned Only"}
          </div>

        </div>
      ))}
    </div>
  );
}

export default SkillsCard;