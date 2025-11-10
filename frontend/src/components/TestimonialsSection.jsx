import '../styles/TestimonialsSection.css';

function TestimonialsSection(){

    return(

        <section id="testimonials" class="py-5">
        <div class="container">
            <div class="text-center mb-5">
            <h2 class="fw-bold">Testimonials</h2>
            <p class="text-muted">What people say about me</p>
            </div>

            <div id="testimonialCarousel" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">

                <div class="carousel-item active">
                <div class="testimonial-card mx-auto text-center p-4 rounded-3 shadow-sm">
                    <img src="person1.jpg" alt="Client" class="rounded-circle mb-3" width="80" height="80" />
                    <p class="fst-italic text-muted">
                    “Ome is a passionate and dedicated developer. His attention to detail and consistent improvement make him a pleasure to work with.”
                    </p>
                    <h6 class="fw-bold mb-0">— Rafiq Ahmed</h6>
                    <small class="text-primary">Project Manager, PQC</small>
                </div>
                </div>

                <div class="carousel-item">
                <div class="testimonial-card mx-auto text-center p-4 rounded-3 shadow-sm">
                    <img src="person2.jpg" alt="Client" class="rounded-circle mb-3" width="80" height="80" />
                    <p class="fst-italic text-muted">
                    “A quick learner and strong problem solver. His Django and React-based projects show both creativity and technical depth.”
                    </p>
                    <h6 class="fw-bold mb-0">— Sarah Rahman</h6>
                    <small class="text-primary">Software Engineer, Freelance</small>
                </div>
                </div>

                <div class="carousel-item">
                <div class="testimonial-card mx-auto text-center p-4 rounded-3 shadow-sm">
                    <img src="person3.jpg" alt="Client" class="rounded-circle mb-3" width="80" height="80" />
                    <p class="fst-italic text-muted">
                    “Ome’s professionalism and coding standards are outstanding. He always delivers clean, efficient, and scalable solutions.”
                    </p>
                    <h6 class="fw-bold mb-0">— Kamal Uddin</h6>
                    <small class="text-primary">Senior Developer, TechForge</small>
                </div>
                </div>

            </div>

            <button class="carousel-control-prev" type="button" data-bs-target="#testimonialCarousel" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#testimonialCarousel" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
            </button>

            </div>
        </div>
        </section>

    )
}

export default TestimonialsSection