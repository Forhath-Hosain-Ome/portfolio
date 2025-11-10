

import '../styles/SocialLinksSection.css';

function SocialLinksSection(){
    
    return(
        <>
            <section id="social" class="py-5 bg-light">
            <div class="container text-center">
                <h2 class="fw-bold mb-4">Connect with Me</h2>
                <p class="text-muted mb-4">Follow me on social platforms or reach out directly</p>

                <div class="d-flex justify-content-center flex-wrap gap-3">
                <a href="https://github.com/yourusername" target="_blank" class="social-btn">
                    <i class="bi bi-github"></i> GitHub
                </a>
                <a href="https://www.linkedin.com/in/yourusername" target="_blank" class="social-btn">
                    <i class="bi bi-linkedin"></i> LinkedIn
                </a>
                <a href="https://twitter.com/yourusername" target="_blank" class="social-btn">
                    <i class="bi bi-twitter"></i> Twitter
                </a>
                <a href="mailto:ome@example.com" class="social-btn">
                    <i class="bi bi-envelope-fill"></i> Email
                </a>
                <a href="https://www.instagram.com/yourusername" target="_blank" class="social-btn">
                    <i class="bi bi-instagram"></i> Instagram
                </a>
                </div>
            </div>
            </section>

        </>
    )
}

export default SocialLinksSection
