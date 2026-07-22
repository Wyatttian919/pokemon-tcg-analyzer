import {
    useEffect,
    useState
} from "react";


import { getUserCollection, deleteCollectionItem, updateCollectionItem} from "../api/collectionApi";
import type { CollectionItem} from "../api/collectionApi";



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



            {
                items.map(item=>(

                    <div
                        key={item.id}
                    >


                        <h3>
                            {item.card.name}
                        </h3>



                        {
                            editingId === item.id

                            ?

                            (

                                <>

                                    <input

                                        value={editQuantity}

                                        onChange={
                                            e =>
                                            setEditQuantity(
                                                Number(e.target.value)
                                            )
                                        }

                                    />


                                    <input

                                        value={editCondition}

                                        onChange={
                                            e =>
                                            setEditCondition(
                                                e.target.value
                                            )
                                        }

                                    />


                                    <button
                                        onClick={()=>
                                            handleUpdate(item.id)
                                        }
                                    >
                                        Save
                                    </button>


                                </>

                            )


                            :


                            (

                                <>

                                    <p>
                                        Quantity:
                                        {item.quantity}
                                    </p>


                                    <p>
                                        Condition:
                                        {item.condition}
                                    </p>



                                    <button

                                        onClick={()=>{

                                            setEditingId(
                                                item.id
                                            );


                                            setEditQuantity(
                                                item.quantity
                                            );


                                            setEditCondition(
                                                item.condition
                                            );

                                        }}

                                    >
                                        Edit
                                    </button>


                                </>

                            )

                        }



                        <button

                            onClick={()=>
                                handleDelete(item.id)
                            }

                        >
                            Remove
                        </button>


                    </div>

                ))
            }


        </div>

    );

}


export default CollectionPage;