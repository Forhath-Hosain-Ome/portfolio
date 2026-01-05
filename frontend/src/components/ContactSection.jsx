import '../styles/ContactSection.css';

function ContactSection(){

    return(
        <section id="contact" className="section-padding bg-light">
            <div className="container text-center">
                <h2 className="fw-bold mb-4">Let’s Connect</h2>
                <p className="text-muted mb-5">Got an idea, collaboration, or opportunity? Send me a message!</p>

                <form className="col-md-8 mx-auto">
                <div className="mb-3">
                    <input type="text" className="form-control rounded-pill py-3" placeholder="Your Name" required />
                </div>
                <div className="mb-3">
                    <input type="email" className="form-control rounded-pill py-3" placeholder="Your Email" required />
                </div>
                <div className="mb-3">
                    <textarea className="form-control rounded-4" rows="4" placeholder="Your Message" required></textarea>
                </div>
                <button type="submit" className="btn btn-dark rounded-pill px-5 py-2">Send Message</button>
                </form>

                <div className="mt-4">
                <a href="#" className="text-dark mx-2"><i className="bi bi-github fs-3"></i></a>
                <a href="#" className="text-dark mx-2"><i className="bi bi-linkedin fs-3"></i></a>
                <a href="#" className="text-dark mx-2"><i className="bi bi-envelope fs-3"></i></a>
                </div>
            </div>
        </section>
    )
}

export default ContactSection