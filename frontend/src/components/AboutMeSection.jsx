import '../styles/HeroSection.css';


function HeroSection(){
    return(
        <>
            <section class="about py-5" id="about">
                <div class="container">
                    <div class="row align-items-center justify-content-center">
                    <div class="col-lg-6 mb-4 mb-lg-0">
                        <img src="https://via.placeholder.com/500x400.png?text=About+Me+Image" 
                            alt="About Me" 
                            class="img-fluid rounded shadow-lg" />
                    </div>
                    <div class="col-lg-6">
                        <h2 class="about-title mb-3">About <span>Me</span></h2>
                        <p class="about-intro">
                        I’m a passionate <strong>Frontend Developer</strong> who loves creating 
                        engaging, accessible, and efficient web experiences using modern 
                        technologies. With a strong eye for design and detail, I turn creative ideas 
                        into reality.
                        </p>

                        <div class="about-more collapse" id="aboutMore">
                        <p>
                            My journey started with curiosity about how websites work — from basic 
                            HTML pages to complex dynamic apps. Over the years, I’ve honed my skills 
                            in JavaScript, React, and responsive design. I enjoy collaborating on 
                            creative projects, solving technical challenges, and continually learning 
                            new tools.
                        </p>
                        <p>
                            When I’m not coding, you’ll find me exploring nature, sketching UI 
                            concepts, or reading about tech innovation.
                        </p>
                        </div>

                        <button class="btn-more mt-3" 
                                data-bs-toggle="collapse" 
                                data-bs-target="#aboutMore" 
                                aria-expanded="false" 
                                aria-controls="aboutMore">
                        More About Me
                        </button>
                    </div>
                    </div>
                </div>
                </section>
        </>
    )
}

export default HeroSection