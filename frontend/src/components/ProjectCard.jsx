import "../styles/ProjectCard.css";

function ProjectCard({ projects }) {
  return (
    <div className="project-card">
      <h2>📂 Projects</h2>

      {projects.map((project, index) => (
        <div key={index} className="project">
          <h3>{project.title}</h3>

          <ul>
            {project.description.map((line, i) => (
              <li key={i}>{line}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default ProjectCard;