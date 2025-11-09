import '../styles/SkillSection.css';
import ButtonMain from './ButtonMain.jsx'

function SkillSection(){
    return(
        <>
            <section id="about" className="section bg-light">
  <div className="container">
        <h2 className="section-title">My Skills</h2>
    <div className="row align-items-center">

      
      <div className="col-md-6">
        <div className="mt-4">
          <div className="mb-3">
            <div className="progress progress-custom">
              <div className="progress-bar progress-bar-custom" role="progressbar" style={{width:90 + '%'}} aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            <small className="text-muted-custom">Frontend Development — 90%</small>
          </div>
        </div>
        </div>
      <div className="col-md-6">
          <div className="mb-3">
            <div className="progress progress-custom">
              <div className="progress-bar progress-bar-custom" role="progressbar" style={{width:80 + '%'}} aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            <small className="text-muted-custom">UI/UX Design — 80%</small>
          </div>
        </div>
        <div className="mt-4">
          <ButtonMain label='View Projects'/>
          <ButtonMain label='Contact Me'/>
        </div>
      </div>
      
      </div>
</section>
        </>
    )
}

export default SkillSection