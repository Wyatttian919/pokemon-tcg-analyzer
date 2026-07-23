import { useState } from "react";

import { searchCards } from "../api/cardApi";
import type { CardSearchResult } from "../types/card";   
import CardSearchResultCard from "../components/CardSearchResultCard";
import "../styles/search.css"
import SearchBar from "../components/SearchBar";


function SearchPage() {


    const [cards, setCards] = useState<CardSearchResult[]>([]);



    async function handleSearch(keyword:string) {

        const result = await searchCards(keyword);

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


                <SearchBar
                    onSearch={handleSearch}
                />


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