import "./Navbar.css";

function Navbar() {
    return (
        <nav className="navbar">
            <h2 className="logo">ResumeFit</h2>

            <ul className="nav-links">
                <li>Home</li>
                <li>Features</li>
                <li>About</li>
                <li>Login</li>
            </ul>
</nav>
    );
}

export default Navbar;