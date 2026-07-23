import {Link} from "react-router-dom";
import "../styles/navbar.css";



function Navbar(){


    return (

        <nav className="navbar">

            <h2>
            <div className="navbar-brand">

                <Link to="/">
                    Pokémon TCG Analyzer
                </Link>

            </div>
            </h2>


            <div className="navbar-links">

                <Link to="/">
                    Search
                </Link>


                {" | "}


                <Link to="/collection">
                    Collection
                </Link>


            </div>


        </nav>

    );

}


export default Navbar;