import { useState } from "react";

import { searchCards } from "../api/cardApi";
import type { CardSearchResult } from "../types/card";   
import CardSearchResultCard from "../components/CardSearchResultCard";
import "../styles/card-search.css"


function SearchPage() {


    const [keyword, setKeyword] = useState("");

    const [cards, setCards] = useState<CardSearchResult[]>([]);



    async function handleSearch() {

        const result = await searchCards(
            keyword
        );

        setCards(result);

    }



    return (

    <div className="search-page">


        <section className="search-header">


            <h1>
                Pokémon Card Search
            </h1>


            <p>
                Search your Pokémon cards collection
            </p>



            <div className="search-box">


                <input

                    value={keyword}

                    onChange={
                        (e)=>setKeyword(e.target.value)
                    }

                    placeholder="Search card name"

                />


                <button

                    className="button"

                    onClick={handleSearch}

                >
                    Search

                </button>


            </div>


        </section>



        <section className="search-results">


            {
                cards.map(card=>(

                    <CardSearchResultCard

                        key={card.id}

                        card={card}

                    />

                ))
            }


        </section>


    </div>

);

}


export default SearchPage;