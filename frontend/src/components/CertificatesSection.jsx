


import '../styles/CertificatesSection.css';

function CertificatesSection(){
    
    return(
        <>
            <section id="certificates" class="py-5 bg-light">
            <div class="container">
                <div class="text-center mb-5">
                <h2 class="fw-bold">Certificates & Achievements</h2>
                <p class="text-muted">Recognition of my learning milestones and accomplishments</p>
                </div>

                <div class="row g-4">
                <div class="col-md-6 col-lg-4">
                    <div class="cert-card p-4 text-center shadow-sm rounded-3">
                    <img src="cert1.jpg" alt="Certificate 1" class="img-fluid mb-3 rounded" />
                    <h6 class="fw-bold mb-1">Full Stack Web Development</h6>
                    <small class="text-primary">Coursera, 2023</small>
                    </div>
                </div>

                <div class="col-md-6 col-lg-4">
                    <div class="cert-card p-4 text-center shadow-sm rounded-3">
                    <img src="cert2.jpg" alt="Certificate 2" class="img-fluid mb-3 rounded" />
                    <h6 class="fw-bold mb-1">Django & REST APIs</h6>
                    <small class="text-success">Udemy, 2023</small>
                    </div>
                </div>

                <div class="col-md-6 col-lg-4">
                    <div class="cert-card p-4 text-center shadow-sm rounded-3">
                    <img src="cert3.jpg" alt="Certificate 3" class="img-fluid mb-3 rounded" />
                    <h6 class="fw-bold mb-1">Responsive Web Design</h6>
                    <small class="text-warning">freeCodeCamp, 2022</small>
                    </div>
                </div>
                </div>
            </div>
            </section>

        </>
    )
}

export default CertificatesSection