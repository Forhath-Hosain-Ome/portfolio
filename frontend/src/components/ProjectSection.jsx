import '../styles/ProjectSection.css';

function ProjectSection(){
    return(
        <section id="projects" className="py-5">
            <div className="container">
                <div className="text-center mb-5">
                <h2 className="fw-bold">Projects</h2>
                <p className="text-muted">Some of my recent works and experiments</p>
                </div>
                <div className="row g-4">
                <div className="col-md-4">
                    <div className="card border-0 shadow-sm h-100">
                    <img src="project1.jpg" className="card-img-top" alt="Project 1" />
                    <div className="card-body">
                        <h5 className="card-title">Portfolio Website</h5>
                        <p className="card-text text-muted">A modern personal portfolio built using Bootstrap and Django.</p>
                        <a href="#" className="btn btn-outline-dark btn-sm">View</a>
                    </div>
                    </div>
                </div>
                <div className="col-md-4">
                    <div className="card border-0 shadow-sm h-100">
                    <img src="project2.jpg" className="card-img-top" alt="Project 2" />
                    <div className="card-body">
                        <h5 className="card-title">Worker Management System</h5>
                        <p className="card-text text-muted">A web-based management platform for garments factory operations.</p>
                        <a href="#" className="btn btn-outline-dark btn-sm">View</a>
                    </div>
                    </div>
                </div>
                <div className="col-md-4">
                    <div className="card border-0 shadow-sm h-100">
                    <img src="project3.jpg" className="card-img-top" alt="Project 3" />
                    <div className="card-body">
                        <h5 className="card-title">Medicine Tracker</h5>
                        <p className="card-text text-muted">Track your medicines and reminders using Django and Bootstrap.</p>
                        <a href="#" className="btn btn-outline-dark btn-sm">View</a>
                    </div>
                    </div>
                </div>
                </div>
            </div>
        </section>
        
    )
}

export default ProjectSection
