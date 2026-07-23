import {
    useEffect,
    useState
} from "react";


import { getUserCollection, deleteCollectionItem, updateCollectionItem} from "../api/collectionApi";
import type { CollectionItem} from "../types/collection";
import CollectionItemCard from "../components/CollectionItemCard";
import "../styles/collection.css";


function CollectionPage(){


    const [items,setItems] = useState<CollectionItem[]>([]);
    const [editingId,setEditingId] = useState<number | null>(null);
    const [editQuantity,setEditQuantity] = useState<number>(1);
    const [editCondition,setEditCondition] = useState<string>("");

    useEffect(()=>{


        async function fetchCollection(){

            const data = await getUserCollection(1);

            setItems(data);

        }


        fetchCollection();


    },[]);



    const handleDelete = async (itemId:number)=>{

        await deleteCollectionItem(
            itemId
        );


        setItems(
            items.filter(
                item => item.id !== itemId
            )
        );

    };



    const handleUpdate = async(itemId:number)=>{

        const updated =
            await updateCollectionItem(
                itemId,
                {
                    quantity: editQuantity,
                    condition: editCondition
                }
            );


        setItems(
            items.map(item=>

                item.id === itemId
                ?
                updated
                :
                item

            )
        );


        setEditingId(null);

    };




    return (

        <div>


            <h1>
                My Collection
            </h1>



            <div className="collection-list">

            {
                items.map(item=>(

                    <CollectionItemCard

                        key={item.id}

                        item={item}


                        editing={
                            editingId === item.id
                        }


                        editQuantity={
                            editQuantity
                        }


                        editCondition={
                            editCondition
                        }


                        onEdit={()=>{

                            setEditingId(item.id);


                            setEditQuantity(
                                item.quantity
                            );


                            setEditCondition(
                                item.condition
                            );

                        }}


                        onDelete={()=>handleDelete(item.id)}


                        onSave={()=>handleUpdate(item.id)}


                        setEditQuantity={
                            setEditQuantity
                        }


                        setEditCondition={
                            setEditCondition
                        }


                    />

                ))
            }

            </div>


        </div>

    );

}


export default CollectionPage;