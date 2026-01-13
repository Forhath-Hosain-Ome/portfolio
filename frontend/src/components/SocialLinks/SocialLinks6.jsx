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
        return (
            <a
              className="inline-block"
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

export default SocialLinks6;
