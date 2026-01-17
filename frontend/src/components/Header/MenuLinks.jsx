import { Link } from "react-router-dom";

const MenuLinks = () => {
  return (
    <nav className="relative hidden lg:block">
      <ul className="flex flex-col lg:flex-row gap-4 lg:gap-10">
        <li className="menuItemHasChildren relative group text-[1rem] lg:text-[1.125rem] font-Poppins font-semibold uppercase">
          <Link
            className="hover:text-accent text-accent2 pr-5 relative block"
            to="/"
            title="Home"
          >
            Home
          </Link>
        </li>
        <li className="menuItemHasChildren relative group text-[1rem] lg:text-[1.125rem] font-Poppins font-semibold uppercase">
          <Link
            className="hover:text-accent text-accent2 pr-5 relative block"
            to="/blog/:Id"
            title="Blog"
          >
            Blog
          </Link>
        </li>
        <li className="menuItemHasChildren relative group text-[1rem] lg:text-[1.125rem] font-Poppins font-semibold uppercase">
          <Link
            className="hover:text-accent text-accent2 pr-5 relative block"
            to="/portfolio/:Id"
            title="Portfolio"
          >
            Portfolio
          </Link>
        </li>
        <li className="menuItemHasChildren relative group text-[1rem] lg:text-[1.125rem] font-Poppins font-semibold uppercase">
          <Link
            className="hover:text-accent text-accent2 pr-5 relative block"
            to="/plans"
            title="Plans"
          >
            Plans
          </Link>
        </li>
        <li className="menuItemHasChildren relative group text-[1rem] lg:text-[1.125rem] font-Poppins font-semibold uppercase">
          <Link
            className="hover:text-accent text-accent2 pr-5 relative block"
            to="/service/:Id"
            title="Service"
          >
            Service
          </Link>
        </li>
        <li className="menuItemHasChildren relative group text-[1rem] lg:text-[1.125rem] font-Poppins font-semibold uppercase">
          <Link
            className="group-hover:text-accent text-accent2 pr-5 relative block"
            to="/contact"
            title="Contact"
          >
            Contact
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default MenuLinks;
