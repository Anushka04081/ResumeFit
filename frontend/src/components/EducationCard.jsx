import "../styles/EducationCard.css";

function EducationCard({ education }) {
  return (
    <div className="education-card">
      <h2>🎓 Education</h2>

      {education.length === 0 ? (
        <p>No education details found.</p>
      ) : (
        education.map((item, index) => (
          <div key={index} className="education-item">

            <h3>{item.degree}</h3>

            {item.college && (
              <p>
                <strong>🏫 Institute:</strong> {item.college}
              </p>
            )}

            {item.year && (
              <p>
                <strong>📅 Duration:</strong> {item.year}
              </p>
            )}

            {item.cgpa && (
              <p>
                <strong>⭐ CGPA:</strong> {item.cgpa}
              </p>
            )}

          </div>
        ))
      )}
    </div>
  );
}

export default EducationCard;