import FacebookIcon from "../lib/icons/Facebook.svg?react";
import TumblrIcon from "../lib/icons/Tumblr.svg?react";
import TwitterIcon from "../lib/icons/Twitter.svg?react";

export const social4 = [
  {
    socialIcon: (
      <FacebookIcon className="h-5 w-5 lg:h-10 lg:w-10 fill-accent hover:fill-accent"></FacebookIcon>
    ),
    socialLink: "https://www.facebook.com/",
    socialTitle: "Facebook",
  },
  {
    socialIcon: (
      <TumblrIcon className="h-5 w-5 lg:h-10 lg:w-10 fill-[#3d5a70] hover:fill-accent"></TumblrIcon>
    ),
    socialLink: "#",
    socialTitle: "Tumblr",
  },
  {
    socialIcon: (
      <TwitterIcon className="h-5 w-5 lg:h-10 lg:w-10 fill-[#0ddae1] hover:fill-accent"></TwitterIcon>
    ),
    socialLink: "https://twitter.com/",
    socialTitle: "Twitter",
  },
];
