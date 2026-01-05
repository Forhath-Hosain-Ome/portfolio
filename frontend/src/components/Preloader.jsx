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

		{/* <div class="txt-loading" aria-label="Loading PQC">
		  <span data-text-preloader="F" class="letters-loading">F</span>
		  <span data-text-preloader="O" class="letters-loading">O</span>
		  <span data-text-preloader="R" class="letters-loading">R</span>
		  <span data-text-preloader="H" class="letters-loading">H</span>
		  <span data-text-preloader="A" class="letters-loading">A</span>
		  <span data-text-preloader="T" class="letters-loading">T</span>
		  <span data-text-preloader="H" class="letters-loading">H</span>
		</div> */}

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