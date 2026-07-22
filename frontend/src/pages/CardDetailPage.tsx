import {
    useEffect,
    useState
} from "react";


import {
    useParams
} from "react-router-dom";


import {getCardDetail} from "../api/cardApi";
import type {CardDetail} from "../api/cardApi";
import {addToCollection} from "../api/collectionApi";

function CardDetailPage(){


    const { id } = useParams();


    const [card,setCard] = useState<CardDetail | null>(null);

    const [added,setAdded] = useState(false);

    useEffect(()=>{


        async function fetchCard(){

            if(!id){
                return;
            }


            const data = await getCardDetail(
                Number(id)
            );


            setCard(data);

        }


        fetchCard();


    },[id]);

 

        const handleAddToCollection = async () =>{

            if(!card){
                return;
            }


            await addToCollection({

                user_id:1,

                card_id:card.id,

                quantity:1,

                condition:"Near Mint"

            });


            alert(
                "Added to collection!"
            );

            setAdded(true);

        };



    if(!card){

        return (
            <div>
                Loading...
            </div>
        );

    }



    return (

        <div>


            <h1>
                {card.name}
            </h1>


            <img
                src={card.image_url}
                width="250"
            />


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


            <h3>
                Set
            </h3>


            <p>
                {card.set.name}
            </p>


            <button
                onClick={handleAddToCollection}
            >
                {
                    added
                    ? "Added ✓"
                    : "Add to Collection"
                }
            </button>


        </div>

    );

}


export default CardDetailPage;