import { social3 } from "../../data/social3";

const SocialLinks5 = () => {
  return (
    <div className="socialLinks flex flex-col items-center gap-[5px] absolute right-[3.75rem] bottom-[2.8125rem]">
      {social3.slice(0, 4).map((item, index) =>{
        const IconComponent = item.socialIcon;
        if (typeof IconComponent !== 'function') {
          console.error('IconComponent is not a function:', IconComponent);
          return null;
        }
        return (
            <a
              className={item.socialClass}
              href={item.socialLink}
              title={item.socialTitle}
              target="_blank"
              key={index}
              rel="noreferrer"
            >
              <IconComponent className={`${item.className}`} />
            </a>
          )
        }
      )}
      {/* Social Links */}
    </div>
  );
};

export default SocialLinks5;
