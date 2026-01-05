import '../styles/FooterSection.css';

function FooterSection(){

    return(
        <footer className="footer bg-dark text-light pt-5 pb-4 mt-5">
        <div className="container">
            <div className="row gy-4">
            <div className="col-md-6 col-lg-3">
                <h5 className="fw-bold mb-3 text-uppercase">Forhath Hosain Ome</h5>
                <p className="text-muted small">
                A passionate full-stack developer focused on creating elegant and functional web experiences using Django, React, and modern design principles.
                </p>
                <div className="social-links mt-3">
                <a href="#" className="text-light me-3"><i className="bi bi-github fs-5"></i></a>
                <a href="#" className="text-light me-3"><i className="bi bi-linkedin fs-5"></i></a>
                <a href="#" className="text-light"><i className="bi bi-envelope fs-5"></i></a>
                </div>
            </div>

            <div className="col-md-6 col-lg-3">
                <h5 className="fw-bold mb-3 text-uppercase">Quick Links</h5>
                <ul className="list-unstyled footer-links">
                <li><a href="#about" className="text-decoration-none">About</a></li>
                <li><a href="#skills" className="text-decoration-none">Skills</a></li>
                <li><a href="#projects" className="text-decoration-none">Projects</a></li>
                <li><a href="#contact" className="text-decoration-none">Contact</a></li>
                </ul>
            </div>

            <div className="col-md-6 col-lg-3">
                <h5 className="fw-bold mb-3 text-uppercase">Services</h5>
                <ul className="list-unstyled footer-links">
                <li><a href="#" className="text-decoration-none">Web Development</a></li>
                <li><a href="#" className="text-decoration-none">API Integration</a></li>
                <li><a href="#" className="text-decoration-none">UI/UX Design</a></li>
                <li><a href="#" className="text-decoration-none">Database Design</a></li>
                </ul>
            </div>

            <div className="col-md-6 col-lg-3">
                <h5 className="fw-bold mb-3 text-uppercase">Contact</h5>
                <ul className="list-unstyled small text-muted mb-2">
                <li><i className="bi bi-geo-alt-fill text-primary me-2"></i>Dhaka, Bangladesh</li>
                <li><i className="bi bi-telephone-fill text-primary me-2"></i>+880 1XXX-XXXXXX</li>
                <li><i className="bi bi-envelope-fill text-primary me-2"></i>ome@example.com</li>
                </ul>
                <button className="btn btn-sm btn-primary rounded-pill mt-2 px-4">Hire Me</button>
            </div>
            </div>

            <hr className="border-light opacity-25 mt-5" />

            <div className="text-center pt-3">
            <small className="text-muted">&copy; 2025 Forhath Hosain Ome | Designed with ❤️ using Bootstrap 5</small>
            </div>
        </div>
        </footer>
    )
}

export default FooterSection