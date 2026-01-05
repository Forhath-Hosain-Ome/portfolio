

import '../styles/SocialLinksSection.css';

function SocialLinksSection(){
    
    return(
        <>
            <section id="social" className="py-5 bg-light">
            <div className="container text-center">
                <h2 className="fw-bold mb-4">Connect with Me</h2>
                <p className="text-muted mb-4">Follow me on social platforms or reach out directly</p>

                <div className="d-flex justify-content-center flex-wrap gap-3">
                <a href="https://github.com/yourusername" target="_blank" className="social-btn">
                    <i className="bi bi-github"></i> GitHub
                </a>
                <a href="https://www.linkedin.com/in/yourusername" target="_blank" className="social-btn">
                    <i className="bi bi-linkedin"></i> LinkedIn
                </a>
                <a href="https://twitter.com/yourusername" target="_blank" className="social-btn">
                    <i className="bi bi-twitter"></i> Twitter
                </a>
                <a href="mailto:ome@example.com" className="social-btn">
                    <i className="bi bi-envelope-fill"></i> Email
                </a>
                <a href="https://www.instagram.com/yourusername" target="_blank" className="social-btn">
                    <i className="bi bi-instagram"></i> Instagram
                </a>
                </div>
            </div>
            </section>

        </>
    )
}

export default SocialLinksSection
