import "./Hero.css";

function Hero({ title, description, buttonText }) {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1>{title}</h1>

        <p>{description}</p>

        <button>{buttonText}</button>
      </div>

      <div className="hero-image">
        <img
          src="https://placehold.co/400x300"
          alt="Resume Illustration"
        />
      </div>
    </section>
  );
}

export default Hero;