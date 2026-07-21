import "./Hero.css";

function Hero() {
  return (
    <section className="hero">

      <div className="hero-content">

        <h1>
          Analyze Your Resume
          <span> Like a Recruiter</span>
        </h1>

        <p>
          ResumeFit helps you evaluate your resume, compare it with any
          job description, identify missing skills, and improve your ATS
          score in seconds.
        </p>

        <button>Analyze Resume</button>

      </div>

      <div className="hero-image">

        <img
          src="https://undraw.co/api/illustrations/undraw_resume_re_hkth.svg"
          alt="Resume Analysis"
        />

      </div>

    </section>
  );
}

export default Hero;