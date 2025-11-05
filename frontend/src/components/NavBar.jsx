import '../styles/NavBar.css';

const navigation = ['Home', 'About', 'Projects', 'Contact'];
const navitem = navigation.map(nav =>
    <li>
        <a href="#" className="nav-link">
            {nav}
        </a>
    </li>
)
function NavBar(){
    return(
        <>
            <nav className="navbar navbar-expand-lg navbar-dark sticky-top">
                <div className="container">
                <a className="navbar-brand" href="#">BrandName</a>
                <button className="navbar-toggler collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
                    <ul className="navbar-nav">
                        {navitem}
                    </ul>
                </div>
                </div>
            </nav>
        </>
    )
}

export default NavBar