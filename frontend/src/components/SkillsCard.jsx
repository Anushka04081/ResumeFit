import "../styles/SkillsCard.css";

function SkillsCard({ skills }) {
  return (
    <div className="skills-card">
      <h2>Skills</h2>

      {skills.map((skill, index) => (
        <div key={index} className="skill-row">
          <span>{skill.name}</span>

          {skill.implemented ? (
            <span className="implemented">✅ Implemented</span>
          ) : (
            <span className="not-implemented">❌ Mentioned Only</span>
          )}
        </div>
      ))}
    </div>
  );
}

export default SkillsCard;