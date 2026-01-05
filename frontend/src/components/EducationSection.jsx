import '../styles/EducationSection.css';

function EducationSection(){

    return(
        <>
            <section id="education" className="py-5 bg-light">
            <div className="container">
                <div className="text-center mb-5">
                <h2 className="fw-bold">Education</h2>
                <p className="text-muted">My academic journey and learning milestones</p>
                </div>

                <div className="row g-4">
                <div className="col-md-6 col-lg-4">
                    <div className="edu-card p-4 h-100 shadow-sm rounded-3">
                    <h5 className="fw-bold mb-1">BSc in Computer Science & Engineering</h5>
                    <small className="text-primary fw-semibold">2021 – Present</small>
                    <p className="mt-3 text-muted">Learning core CS concepts including algorithms, databases, full stack web development, and software engineering principles.</p>
                    <p className="fw-medium mb-0">University: <span className="text-dark">[Your University Name]</span></p>
                    </div>
                </div>

                <div className="col-md-6 col-lg-4">
                    <div className="edu-card p-4 h-100 shadow-sm rounded-3">
                    <h5 className="fw-bold mb-1">Full Stack Web Development</h5>
                    <small className="text-success fw-semibold">2022 – 2023</small>
                    <p className="mt-3 text-muted">Completed online bootcamps focused on Django, REST APIs, React.js, and deployment best practices.</p>
                    <p className="fw-medium mb-0">Institute: <span className="text-dark">Online Course Platform</span></p>
                    </div>
                </div>

                <div className="col-md-6 col-lg-4">
                    <div className="edu-card p-4 h-100 shadow-sm rounded-3">
                    <h5 className="fw-bold mb-1">Secondary & Higher Secondary Education</h5>
                    <small className="text-warning fw-semibold">2012 – 2020</small>
                    <p className="mt-3 text-muted">Built a strong base in science and mathematics, which later evolved into my interest in technology and coding.</p>
                    <p className="fw-medium mb-0">Institution: <span className="text-dark">[Your College Name]</span></p>
                    </div>
                </div>
                </div>
            </div>
            </section>
        </>
    )
}

export default EducationSection