import FacebookIcon from "../lib/icons/Facebook.svg?react";
import TumblrIcon from "../lib/icons/Tumblr.svg?react";
import TwitterIcon from "../lib/icons/Twitter.svg?react";

export const social4 = [
  {
    socialIcon: FacebookIcon,
    iconProps: {className: "h-5 w-5 lg:h-10 lg:w-10 fill-accent hover:fill-accent"},
    socialLink: "https://www.facebook.com/",
    socialTitle: "Facebook",
    className: "h-7 w-7 md:h-10 md:w-10 fill-white hover:fill-accent2",
  },
  {
    socialIcon: TumblrIcon,
    iconProps: {className: "h-5 w-5 lg:h-10 lg:w-10 fill-[#3d5a70] hover:fill-accent"},
    socialLink: "#",
    socialTitle: "Tumblr",
    className: "h-7 w-7 md:h-10 md:w-10 fill-white hover:fill-accent2",
  },
  {
    socialIcon: TwitterIcon,
    iconProps: {className: "h-5 w-5 lg:h-10 lg:w-10 fill-[#0ddae1] hover:fill-accent"},
    socialLink: "https://twitter.com/",
    socialTitle: "Twitter",
    className: "h-7 w-7 md:h-10 md:w-10 fill-white hover:fill-accent2",
  },
];
