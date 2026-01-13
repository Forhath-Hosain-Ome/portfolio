import HappyCustomersIcon from "../lib/icons/HappyCustomers.svg?react";
import FinishedProjectsIcon from "../lib/icons/FinishedProjects.svg?react";
import CoffeeCupIcon from "../lib/icons/CoffeeCup.svg?react";
import WorkingHoursIcon from "../lib/icons/WorkingHours.svg?react";

export const funFacts = [
  {
    factIcon: <HappyCustomersIcon className="w-[3.125rem] fill-accent"></HappyCustomersIcon>,
    factCount: "35000",
    factCap: "Happy Customers",
  },
  {
    factIcon: <FinishedProjectsIcon className="w-[3.125rem] fill-accent"></FinishedProjectsIcon>,
    factCount: "15250",
    factCap: "Finished Projects",
  },
  {
    factIcon: <CoffeeCupIcon className="w-[3.125rem] fill-accent"></CoffeeCupIcon>,
    factCount: "927",
    factCap: "Coffee Cups",
  },
  {
    factIcon: <WorkingHoursIcon className="w-[3.125rem] fill-accent"></WorkingHoursIcon>,
    factCount: "52300",
    factCap: "Working Hours",
  },
];
