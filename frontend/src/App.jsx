import Hero from "./components/Hero";
import Navbar from "./components/Navbar";
import "./App.css";

function App() {
  return (
    <div className="container">

      <Navbar />

      <Hero
  title="Analyze Your Resume with AI"
  description="Get instant feedback, ATS score, and personalized suggestions to improve your resume."
  buttonText="Upload Resume"
/>

    </div>
  );
}

export default App;