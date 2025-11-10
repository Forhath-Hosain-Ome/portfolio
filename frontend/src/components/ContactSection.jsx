import '../styles/ContactSection.css';

function ContactSection(){

    return(
        <section id="contact" class="section-padding bg-light">
            <div class="container text-center">
                <h2 class="fw-bold mb-4">Let’s Connect</h2>
                <p class="text-muted mb-5">Got an idea, collaboration, or opportunity? Send me a message!</p>

                <form class="col-md-8 mx-auto">
                <div class="mb-3">
                    <input type="text" class="form-control rounded-pill py-3" placeholder="Your Name" required />
                </div>
                <div class="mb-3">
                    <input type="email" class="form-control rounded-pill py-3" placeholder="Your Email" required />
                </div>
                <div class="mb-3">
                    <textarea class="form-control rounded-4" rows="4" placeholder="Your Message" required></textarea>
                </div>
                <button type="submit" class="btn btn-dark rounded-pill px-5 py-2">Send Message</button>
                </form>

                <div class="mt-4">
                <a href="#" class="text-dark mx-2"><i class="bi bi-github fs-3"></i></a>
                <a href="#" class="text-dark mx-2"><i class="bi bi-linkedin fs-3"></i></a>
                <a href="#" class="text-dark mx-2"><i class="bi bi-envelope fs-3"></i></a>
                </div>
            </div>
        </section>
    )
}

export default ContactSection