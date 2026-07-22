import { useState } from "react";
import { Link } from "react-router-dom";

import { searchCards} from "../api/cardApi";
import type { CardSearchResult } from "../api/cardApi";   


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

        <div>

            <h1>
                Pokémon Card Search
            </h1>


            <input

                value={keyword}

                onChange={
                    (e) => setKeyword(e.target.value)
                }

                placeholder="Search card name"

            />


            <button
                onClick={handleSearch}
            >
                Search
            </button>



            {
                cards.map(
                    card => (

                        <div key={card.id}>

                        
                            <Link to={`/cards/${card.id}`}>
                                <h3>
                                    {card.name}
                                </h3>
                            </Link>


                            <p>
                                #{card.number}
                            </p>


                            <p>
                                {card.rarity}
                            </p>


                        </div>

                    )
                )
            }


        </div>

    );

}


export default SearchPage;