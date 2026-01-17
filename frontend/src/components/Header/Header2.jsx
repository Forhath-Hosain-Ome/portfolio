import { useLayoutEffect, useRef } from "react";
import { Link } from "react-router-dom";
import Logo2 from "../../assets/images/logo2.png";
import { ResponsiveHeader } from "../ResponsiveHeader";
import { SocialLinks2 } from "../SocialLinks";
import MenuLinks from "./MenuLinks";

const Header2 = () => {
  const refHeader = useRef(null);
  
  useLayoutEffect(() => {
    const header = document.getElementById("header2");
    if (!refHeader.current || !header) return;
    
    const fixedTop = refHeader.current.offsetTop;
    
    const stickyHeader = () => {
      if (window.pageYOffset > fixedTop) {
        header.classList.add(
          "stickyHeader",
          "bg-white/80",
          "drop-shadow-2xl",
          "py-3",
          "backdrop-blur-sm"
        );
      } else {
        header.classList.remove(
          "stickyHeader",
          "bg-white/80",
          "drop-shadow-2xl",
          "py-3",
          "backdrop-blur-sm"
        );
      }
    };
    
    window.addEventListener("scroll", stickyHeader);
    
    // Cleanup function
    return () => {
      window.removeEventListener("scroll", stickyHeader);
    };
  }, []);

  return (
    <>
      <header
        className="fixed transition-all ease-in duration-300 top-0 left-0 w-full py-8 z-[9999] hidden lg:block"
        ref={refHeader}
        id="header2"
      >
        <div className="logoMenu w-full">
          <div className="container sm:container md:container lg:container xl:container 2xl:max-w-[100rem] mx-auto">
            <div className="logoMenuInner flex items-center justify-between relative w-full">
              <div className="logo inline-block max-w-[50%]">
                <Link to="/" title="Fastone">
                  <img src={Logo2} alt="Logo" />
                </Link>
              </div>
              <MenuLinks />
              <div className="menuRight hidden lg:flex items-center gap-8 lg:gap-12">
                <SocialLinks2 />
                <Link
                  className="bg-transparent border-2 border-current text-accent text-[1rem] font-Poppins font-bold uppercase rounded-[5px] md:rounded-[10px] md:px-6 lg:px-10 xl:px-11 px-7 md:py-[1rem] py-[10px] hover:bg-accent hover:border-accent hover:text-white text-center inline-block"
                  to="/"
                  title="Download CV"
                >
                  Download CV
                </Link>
              </div>
            </div>
          </div>
        </div>
      </header>
      <ResponsiveHeader />
    </>
  );
};

export default Header2;