import { Link } from "react-router-dom";

import "../styles/home.css";


function HomePage(){


    return (

        <div className="home">


            <section className="hero">


                <h1>
                    Pokémon TCG Analyzer
                </h1>


                <p>
                    Discover cards, manage your collection,
                    and analyze your Pokémon TCG journey.
                </p>


                <Link
                    to="/search"
                    className="button"
                >
                    Search Cards
                </Link>


            </section>



            <section className="home-actions">


                <Link
                    to="/search"
                    className="card-container home-card"
                >

                    <h3>
                        Search Cards
                    </h3>

                    <p>
                        Find Pokémon cards by name.
                    </p>

                </Link>



                <Link
                    to="/collection"
                    className="card-container home-card"
                >

                    <h3>
                        My Collection
                    </h3>

                    <p>
                        Manage your card collection.
                    </p>

                </Link>


            </section>


        </div>

    );

}


export default HomePage;