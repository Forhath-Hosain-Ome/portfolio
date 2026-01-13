import { social2 } from "../../data/social2";

const SocialLinks2 = () => {
  return (
    <div className="socialLinks flex items-center gap-[5px]">
      {social2.slice(0, 3).map((item, index) =>{
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
                <IconComponent className="h-7 w-7 md:h-10 md:w-10 fill-white hover:fill-accent2" />
              </a>
            )
        }
      )}
      {/* Social Links */}
    </div>
  );
};

export default SocialLinks2;
