import '../styles/EducationSection.css';

function EducationSection(){

    return(
        <>
            <section id="education" class="py-5 bg-light">
            <div class="container">
                <div class="text-center mb-5">
                <h2 class="fw-bold">Education</h2>
                <p class="text-muted">My academic journey and learning milestones</p>
                </div>

                <div class="row g-4">
                <div class="col-md-6 col-lg-4">
                    <div class="edu-card p-4 h-100 shadow-sm rounded-3">
                    <h5 class="fw-bold mb-1">BSc in Computer Science & Engineering</h5>
                    <small class="text-primary fw-semibold">2021 – Present</small>
                    <p class="mt-3 text-muted">Learning core CS concepts including algorithms, databases, full stack web development, and software engineering principles.</p>
                    <p class="fw-medium mb-0">University: <span class="text-dark">[Your University Name]</span></p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-4">
                    <div class="edu-card p-4 h-100 shadow-sm rounded-3">
                    <h5 class="fw-bold mb-1">Full Stack Web Development</h5>
                    <small class="text-success fw-semibold">2022 – 2023</small>
                    <p class="mt-3 text-muted">Completed online bootcamps focused on Django, REST APIs, React.js, and deployment best practices.</p>
                    <p class="fw-medium mb-0">Institute: <span class="text-dark">Online Course Platform</span></p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-4">
                    <div class="edu-card p-4 h-100 shadow-sm rounded-3">
                    <h5 class="fw-bold mb-1">Secondary & Higher Secondary Education</h5>
                    <small class="text-warning fw-semibold">2012 – 2020</small>
                    <p class="mt-3 text-muted">Built a strong base in science and mathematics, which later evolved into my interest in technology and coding.</p>
                    <p class="fw-medium mb-0">Institution: <span class="text-dark">[Your College Name]</span></p>
                    </div>
                </div>
                </div>
            </div>
            </section>
        </>
    )
}

export default EducationSection