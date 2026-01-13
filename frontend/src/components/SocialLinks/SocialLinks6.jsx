import { social4 } from "../../data/social4";

const SocialLinks6 = () => {
  return (
    <div className="socialLinks flex flex-col items-center justify-center gap-5">
      {social4.slice(0, 3).map((item, index) =>{
        const IconComponent = item.socialIcon;
        if (typeof IconComponent !== 'function') {
          console.error('IconComponent is not a function:', IconComponent);
          return null;
        }
        else console.log("Hello")
        return (
            <a
              className="inline-block"
              href={item.socialLink}
              title={item.socialTitle}
              target="_blank"
              key={index}
              rel="noreferrer"
            >
              <IconComponent className="h-7 w-7 md:h-10 md:w-10 fill-white hover:fill-accent2" />
              {/* {item.socialIcon} */}
            </a>
          )
        }
      )}
      {/* Social Links */}
    </div>
  );
};

export default SocialLinks6;
