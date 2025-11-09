import '../styles/SkillSection.css';
import ButtonMain from './ButtonMain.jsx'

function SkillSection(){
    return(
        <section id="skills" className="section">
  <div className="container">
    <div className="text-center mb-5">
      <h2 className="section-title">Skills</h2>
      <p className="text-muted-custom">A mix of technical expertise and creative problem-solving abilities.</p>
    </div>

    <div className="row g-4">
        
      <div className="col-md-6 col-lg-4">
        <div className="skill-card text-center">
          <div className="skill-icon mb-3">
            <i className="bi bi-code-slash"></i>
          </div>
          <h5 className="skill-title">Frontend Development</h5>

          <div className="text-start">
            <div className="skill-progress">
              <div className="skill-progress-bar" style={{width:90 + '%'}}></div>
            </div>
            <p className="skill-level">HTML / CSS / JavaScript — 90%</p>

            <div className="skill-progress">
              <div className="skill-progress-bar" style={{width:85 + '%'}}></div>
            </div>
            <p className="skill-level">Bootstrap / React — 85%</p>
          </div>
        </div>
      </div>


      <div className="col-md-6 col-lg-4">
        <div className="skill-card text-center">
          <div className="skill-icon mb-3">
            <i className="bi bi-server"></i>
          </div>
          <h5 className="skill-title">Backend Development</h5>

          <div className="text-start">
            <div className="skill-progress">
              <div className="skill-progress-bar" style={{width:80 + '%'}}></div>
            </div>
            <p className="skill-level">Node.js / Express — 80%</p>

            <div className="skill-progress">
              <div className="skill-progress-bar" style={{width:70 + '%'}}></div>
            </div>
            <p className="skill-level">Databases (MongoDB / SQL) — 70%</p>
          </div>
        </div>
      </div>


      <div className="col-md-6 col-lg-4">
        <div className="skill-card text-center">
          <div className="skill-icon mb-3">
            <i className="bi bi-palette"></i>
          </div>
          <h5 className="skill-title">UI / UX & Design</h5>

          <div className="text-start">
            <div className="skill-progress">
              <div className="skill-progress-bar" style={{width:85 + '%'}}></div>
            </div>
            <p className="skill-level">Figma / Adobe XD — 85%</p>

            <div className="skill-progress">
              <div className="skill-progress-bar" style={{width:75 + '%'}}></div>
            </div>
            <p className="skill-level">Branding & Prototyping — 75%</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
    )
}

export default SkillSection;