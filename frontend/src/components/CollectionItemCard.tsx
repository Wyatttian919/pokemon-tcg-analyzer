import type { CollectionItem } from "../types/collection";

import "../styles/collection.css";


interface CollectionItemCardProps {

    item: CollectionItem;

    editing: boolean;

    editQuantity: number;

    editCondition: string;


    onEdit: () => void;

    onDelete: () => void;

    onSave: () => void;


    setEditQuantity: (value:number)=>void;

    setEditCondition: (value:string)=>void;

}



function CollectionItemCard(
    {
        item,
        editing,
        editQuantity,
        editCondition,
        onEdit,
        onDelete,
        onSave,
        setEditQuantity,
        setEditCondition

    }: CollectionItemCardProps
){


    return (

        <div className="card-container collection-card">


            <img

                className="collection-image"

                src={item.card.image_url}

            />



            <h3>

                {item.card.name}

            </h3>



            <p>

                #{item.card.number}

            </p>



            {
                editing

                ?

                (

                    <div className="collection-edit">


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

                            className="button"

                            onClick={onSave}

                        >

                            Save

                        </button>


                    </div>

                )


                :

                (

                    <>


                        <p>

                            Quantity:
                            {" "}
                            {item.quantity}

                        </p>



                        <p>

                            Condition:
                            {" "}
                            {item.condition}

                        </p>



                        <div className="collection-actions">


                            <button

                                className="button"

                                onClick={onEdit}

                            >

                                Edit

                            </button>



                            <button

                                className="button button-danger"

                                onClick={onDelete}

                            >

                                Delete

                            </button>


                        </div>


                    </>

                )

            }


        </div>

    );

}


export default CollectionItemCard;