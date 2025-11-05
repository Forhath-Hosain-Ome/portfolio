import '../styles/HeroSection.css';
import ButtonMain from './ButtonMain.jsx'

function HeroSection(){
    return(
        <>
            <section className="hero d-flex align-items-center">
                <div className="container hero-content">
                <div className="row align-items-center">
                    <div className="col-lg-6">
                        <h1>Hello, I'm <span>Forhath Hosain Ome</span></h1>
                        <p>A passionate <strong>Web Developer</strong> crafting beautiful and functional digital experiences.</p>
                        < ButtonMain ButtonName='View My Work'/>
                    </div>
                    <div className="col-lg-6 text-center mt-4 mt-lg-0">
                        <img src="https://scontent.fdac13-1.fna.fbcdn.net/v/t39.30808-6/504116717_1266068768265837_2587640546485125192_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=4MJPK8I9gH0Q7kNvwFw-hFm&_nc_oc=AdnQW9CfyaT5PcVN0hM_xD3zDE5Wz89animV1QWT9tSkNuqPMQ_n4zUGjnc7o3gOzM4&_nc_zt=23&_nc_ht=scontent.fdac13-1.fna&_nc_gid=orzh8jQnZiEPZycdEbLq9w&oh=00_AfhhAy43kUCwQZTovqnJNB1mlrNv8vuvTQzK2oS32Gqhzw&oe=69115201" alt="Profile Picture" />
                    </div>
                </div>
                </div>
            </section>
        </>
    )
}

export default HeroSection