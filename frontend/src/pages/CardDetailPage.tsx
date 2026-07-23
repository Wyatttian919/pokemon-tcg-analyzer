import {
    useEffect,
    useState
} from "react";


import {
    useParams
} from "react-router-dom";


import {getCardDetail} from "../api/cardApi";
import type {CardDetail} from "../types/card";
import {addToCollection} from "../api/collectionApi";
import CardDetailCard from "../components/CardDetailCard";

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

            <CardDetailCard

                card={card}

                onAdd={handleAddToCollection}

                added={added}

            />

    
        </div>

    );

}


export default CardDetailPage;