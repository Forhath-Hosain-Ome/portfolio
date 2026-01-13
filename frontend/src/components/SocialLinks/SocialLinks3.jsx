import { social } from "../../data/social";

const SocialLinks3 = () => {
  return (
    <div className="socialLinksWrap flex gap-6 items-center">
      <h5 className="text-white font-Poppins font-bold text-[0.984375rem] uppercase">
        Follow Me
      </h5>
      <div className="socialLinks flex items-center gap-[5px]">
        {social.slice(0, 3).map((item, index) =>{
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
      {/* Social Links Wrap */}
    </div>
  );
};

export default SocialLinks3;
