import "../styles/EducationCard.css";

function EducationCard({ education }) {
  return (
    <div className="education-card">
      <h2>🎓 Education</h2>

      {education.map((item, index) => (
        <div key={index} className="education-item">
          <p><strong>Degree:</strong> {item.degree}</p>
          <p><strong>College:</strong> {item.college}</p>
          <p><strong>CGPA:</strong> {item.cgpa}</p>
          <p><strong>Year:</strong> {item.year}</p>
        </div>
      ))}
    </div>
  );
}

export default EducationCard;