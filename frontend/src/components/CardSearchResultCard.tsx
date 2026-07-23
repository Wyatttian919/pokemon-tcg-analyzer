import { Link } from "react-router-dom";

import type { CardSearchResult } from "../types/card";

import "../styles/search.css";


interface CardSearchResultCardProps {

    card: CardSearchResult;

}



function CardSearchResultCard(
    {
        card
    }: CardSearchResultCardProps
){


    return (

        <div className="card-container search-card">


            <Link to={`/cards/${card.id}`}>


                <img
                    className="search-card-image"
                    src={card.image_url}
                />


                <h3>
                    {card.name}
                </h3>


                <p>
                    #{card.number}
                </p>


                <span className="rarity-badge">

                    {card.rarity}

                </span>


            </Link>


        </div>

    );

}


export default CardSearchResultCard;