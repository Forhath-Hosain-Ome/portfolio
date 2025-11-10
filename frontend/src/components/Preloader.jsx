import '../styles/Preloader.css';


function Preloader(){
	    
    return(
        <div id="preloader" class="preloader" aria-hidden="true">
	  <div class="animation-preloader">
		
		<div class="pulse-spinner">
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

		<p class="text-center">Loading</p>
	  </div>

	  <div class="loader" aria-hidden="true">
		<div class="row">
		  <div class="col-3 loader-section section-left"><div class="bg"></div></div>
		  <div class="col-3 loader-section section-left"><div class="bg"></div></div>
		  <div class="col-3 loader-section section-right"><div class="bg"></div></div>
		  <div class="col-3 loader-section section-right"><div class="bg"></div></div>
		</div>
	  </div>
	</div>
    )
}

export default Preloader