import '../styles/TestimonialsSection.css';

function TestimonialsSection(){

    return(

        <section id="testimonials" className="py-5">
        <div className="container">
            <div className="text-center mb-5">
            <h2 className="fw-bold">Testimonials</h2>
            <p className="text-muted">What people say about me</p>
            </div>

            <div id="testimonialCarousel" className="carousel slide" data-bs-ride="carousel">
            <div className="carousel-inner">

                <div className="carousel-item active">
                <div className="testimonial-card mx-auto text-center p-4 rounded-3 shadow-sm">
                    <img src="person1.jpg" alt="Client" className="rounded-circle mb-3" width="80" height="80" />
                    <p className="fst-italic text-muted">
                    “Ome is a passionate and dedicated developer. His attention to detail and consistent improvement make him a pleasure to work with.”
                    </p>
                    <h6 className="fw-bold mb-0">— Rafiq Ahmed</h6>
                    <small className="text-primary">Project Manager, PQC</small>
                </div>
                </div>

                <div className="carousel-item">
                <div className="testimonial-card mx-auto text-center p-4 rounded-3 shadow-sm">
                    <img src="person2.jpg" alt="Client" className="rounded-circle mb-3" width="80" height="80" />
                    <p className="fst-italic text-muted">
                    “A quick learner and strong problem solver. His Django and React-based projects show both creativity and technical depth.”
                    </p>
                    <h6 className="fw-bold mb-0">— Sarah Rahman</h6>
                    <small className="text-primary">Software Engineer, Freelance</small>
                </div>
                </div>

                <div className="carousel-item">
                <div className="testimonial-card mx-auto text-center p-4 rounded-3 shadow-sm">
                    <img src="person3.jpg" alt="Client" className="rounded-circle mb-3" width="80" height="80" />
                    <p className="fst-italic text-muted">
                    “Ome’s professionalism and coding standards are outstanding. He always delivers clean, efficient, and scalable solutions.”
                    </p>
                    <h6 className="fw-bold mb-0">— Kamal Uddin</h6>
                    <small className="text-primary">Senior Developer, TechForge</small>
                </div>
                </div>

            </div>

            <button className="carousel-control-prev" type="button" data-bs-target="#testimonialCarousel" data-bs-slide="prev">
                <span className="carousel-control-prev-icon" aria-hidden="true"></span>
            </button>
            <button className="carousel-control-next" type="button" data-bs-target="#testimonialCarousel" data-bs-slide="next">
                <span className="carousel-control-next-icon" aria-hidden="true"></span>
            </button>

            </div>
        </div>
        </section>

    )
}

export default TestimonialsSection