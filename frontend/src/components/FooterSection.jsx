import '../styles/FooterSection.css';

function FooterSection(){

    return(
        <footer class="footer bg-dark text-light pt-5 pb-4 mt-5">
        <div class="container">
            <div class="row gy-4">
            <div class="col-md-6 col-lg-3">
                <h5 class="fw-bold mb-3 text-uppercase">Forhath Hosain Ome</h5>
                <p class="text-muted small">
                A passionate full-stack developer focused on creating elegant and functional web experiences using Django, React, and modern design principles.
                </p>
                <div class="social-links mt-3">
                <a href="#" class="text-light me-3"><i class="bi bi-github fs-5"></i></a>
                <a href="#" class="text-light me-3"><i class="bi bi-linkedin fs-5"></i></a>
                <a href="#" class="text-light"><i class="bi bi-envelope fs-5"></i></a>
                </div>
            </div>

            <div class="col-md-6 col-lg-3">
                <h5 class="fw-bold mb-3 text-uppercase">Quick Links</h5>
                <ul class="list-unstyled footer-links">
                <li><a href="#about" class="text-decoration-none">About</a></li>
                <li><a href="#skills" class="text-decoration-none">Skills</a></li>
                <li><a href="#projects" class="text-decoration-none">Projects</a></li>
                <li><a href="#contact" class="text-decoration-none">Contact</a></li>
                </ul>
            </div>

            <div class="col-md-6 col-lg-3">
                <h5 class="fw-bold mb-3 text-uppercase">Services</h5>
                <ul class="list-unstyled footer-links">
                <li><a href="#" class="text-decoration-none">Web Development</a></li>
                <li><a href="#" class="text-decoration-none">API Integration</a></li>
                <li><a href="#" class="text-decoration-none">UI/UX Design</a></li>
                <li><a href="#" class="text-decoration-none">Database Design</a></li>
                </ul>
            </div>

            <div class="col-md-6 col-lg-3">
                <h5 class="fw-bold mb-3 text-uppercase">Contact</h5>
                <ul class="list-unstyled small text-muted mb-2">
                <li><i class="bi bi-geo-alt-fill text-primary me-2"></i>Dhaka, Bangladesh</li>
                <li><i class="bi bi-telephone-fill text-primary me-2"></i>+880 1XXX-XXXXXX</li>
                <li><i class="bi bi-envelope-fill text-primary me-2"></i>ome@example.com</li>
                </ul>
                <button class="btn btn-sm btn-primary rounded-pill mt-2 px-4">Hire Me</button>
            </div>
            </div>

            <hr class="border-light opacity-25 mt-5" />

            <div class="text-center pt-3">
            <small class="text-muted">&copy; 2025 Forhath Hosain Ome | Designed with ❤️ using Bootstrap 5</small>
            </div>
        </div>
        </footer>
    )
}

export default FooterSection