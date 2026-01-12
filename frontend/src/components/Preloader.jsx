import '../styles/Preloader.css';


function Preloader(){
	    
    return(
        <div id="preloader" className="preloader" aria-hidden="true">
	  <div className="animation-preloader">
		
		<div className="pulse-spinner">
		  <div></div>
		  <div></div>
		  <div></div>
		  <div></div>
		</div>

		<p className="text-center">Loading</p>
	  </div>

	  <div className="loader" aria-hidden="true">
		<div className="row">
		  <div className="col-3 loader-section section-left"><div className="bg"></div></div>
		  <div className="col-3 loader-section section-left"><div className="bg"></div></div>
		  <div className="col-3 loader-section section-right"><div className="bg"></div></div>
		  <div className="col-3 loader-section section-right"><div className="bg"></div></div>
		</div>
	  </div>
	</div>
    )
}

export default Preloader