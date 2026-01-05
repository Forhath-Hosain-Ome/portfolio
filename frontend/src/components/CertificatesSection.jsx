


import '../styles/CertificatesSection.css';

function CertificatesSection(){
    
    return(
        <>
            <section id="certificates" className="py-5 bg-light">
            <div className="container">
                <div className="text-center mb-5">
                <h2 className="fw-bold">Certificates & Achievements</h2>
                <p className="text-muted">Recognition of my learning milestones and accomplishments</p>
                </div>

                <div className="row g-4">
                <div className="col-md-6 col-lg-4">
                    <div className="cert-card p-4 text-center shadow-sm rounded-3">
                    <img src="cert1.jpg" alt="Certificate 1" className="img-fluid mb-3 rounded" />
                    <h6 className="fw-bold mb-1">Full Stack Web Development</h6>
                    <small className="text-primary">Coursera, 2023</small>
                    </div>
                </div>

                <div className="col-md-6 col-lg-4">
                    <div className="cert-card p-4 text-center shadow-sm rounded-3">
                    <img src="cert2.jpg" alt="Certificate 2" className="img-fluid mb-3 rounded" />
                    <h6 className="fw-bold mb-1">Django & REST APIs</h6>
                    <small className="text-success">Udemy, 2023</small>
                    </div>
                </div>

                <div className="col-md-6 col-lg-4">
                    <div className="cert-card p-4 text-center shadow-sm rounded-3">
                    <img src="cert3.jpg" alt="Certificate 3" className="img-fluid mb-3 rounded" />
                    <h6 className="fw-bold mb-1">Responsive Web Design</h6>
                    <small className="text-warning">freeCodeCamp, 2022</small>
                    </div>
                </div>
                </div>
            </div>
            </section>

        </>
    )
}

export default CertificatesSection