import '../styles/ExperienceSection.css';

function ExperienceSection(){

    return(
        <>
            <section id="experience" className="py-5">
                <div className="container">
                    <div className="text-center mb-5">
                        <h2 className="fw-bold">Experience</h2>
                        <p className="text-muted">My journey through learning and professional experiences</p>
                    </div>

                    <div className="timeline">
                    <div className="timeline-item">
                        <div className="timeline-icon bg-primary"></div>
                        <div className="timeline-content">
                        <h5 className="fw-bold">Reporting Officer – PQC</h5>
                        <small className="text-muted">2023 – Present</small>
                        <p>Working as a Reporting Officer where I handle production and quality control reports, data analysis, and process optimization for garments inspection workflow.</p>
                        </div>
                    </div>

                    <div className="timeline-item">
                        <div className="timeline-icon bg-success"></div>
                        <div className="timeline-content">
                        <h5 className="fw-bold">Full Stack Developer (Freelance)</h5>
                        <small className="text-muted">2022 – 2023</small>
                        <p>Built responsive and data-driven web applications using Django, React, and Bootstrap. Focused on backend logic and clean UI development.</p>
                        </div>
                    </div>

                    <div className="timeline-item">
                        <div className="timeline-icon bg-warning"></div>
                        <div className="timeline-content">
                        <h5 className="fw-bold">CSE Student – BSc in Computer Science & Engineering</h5>
                        <small className="text-muted">Ongoing</small>
                        <p>Studying core computer science concepts like data structures, algorithms, databases, and full stack development to build strong technical foundations.</p>
                        </div>
                    </div>
                    </div>
                </div>
            </section>
        </>
    )
}

export default ExperienceSection