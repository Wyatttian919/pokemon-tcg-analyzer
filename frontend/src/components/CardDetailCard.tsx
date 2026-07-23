import type { CardDetail } from "../types/card";
import "../styles/card-detail.css";


interface CardDetailCardProps {

    card: CardDetail;

    onAdd: () => void;

    added: boolean;

}



function CardDetailCard(
    {
        card,
        onAdd,
        added
    }: CardDetailCardProps
){


    return (

        <div className="card-container card-detail">


            <h1>
                {card.name}
            </h1>



            <div className="card-detail-content">


                <div className="card-image-section">


                    <img

                        className="card-image"

                        src={card.image_url}

                    />


                </div>




                <div className="card-info-section">


                    <p>
                        Number: #{card.number}
                    </p>


                    <p>
                        Rarity: {card.rarity}
                    </p>


                    <p>
                        HP: {card.hp}
                    </p>


                    <p>
                        Type: {card.card_type}
                    </p>


                    <button

                        className="button"

                        onClick={onAdd}

                        disabled={added}

                    >

                        {
                            added
                            ?
                            "Added ✓"
                            :
                            "Add to Collection"
                        }
                        
                    </button>


                </div>


            </div>




            <div className="set-info">


                <h3>
                    Set
                </h3>


                <p>
                    {card.set.name}
                </p>


            </div>



        </div>

    );

}


export default CardDetailCard;