import FacebookIcon  from "../lib/icons/Facebook.svg?react";
import TumblrIcon from "../lib/icons/Tumblr.svg?react";
import TwitterIcon from "../lib/icons/Twitter.svg?react";

export const social2 = [
  {
    socialIcon: (
      <FacebookIcon className="h-5 w-5 lg:h-8 lg:w-8 fill-accent2 hover:fill-accent"></FacebookIcon>
    ),
    socialLink: "https://www.facebook.com/",
    socialTitle: "Facebook",
  },
  {
    socialIcon: (
      <TumblrIcon className="h-5 w-5 lg:h-8 lg:w-8 fill-accent2 hover:fill-accent"></TumblrIcon>
    ),
    socialLink: "#",
    socialTitle: "Tumblr",
  },
  {
    socialIcon: (
      <TwitterIcon className="h-5 w-5 lg:h-8 lg:w-8 fill-accent2 hover:fill-accent"></TwitterIcon>
    ),
    socialLink: "https://twitter.com/",
    socialTitle: "Twitter",
  },
];
