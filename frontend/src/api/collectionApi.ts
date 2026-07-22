import axios from "axios";


const API = axios.create({

    baseURL:"http://localhost:8000"

});



export interface CollectionItem {

    id:number;
    quantity:number;
    condition:string;
    purchase_price?:number;

    card:{

        id:number;
        name:string;
        number:string;

    };

}



export interface CollectionItemCreate {

    user_id:number;
    card_id:number;
    quantity:number;
    condition:string;

}



export interface CollectionItemUpdate {

    quantity?: number;
    condition?: string;

}



export async function getUserCollection(
    userId:number
):Promise<CollectionItem[]> {


    const response = await API.get(
        `/users/${userId}/collection`
    );


    return response.data;

}



export async function addToCollection(
    data:CollectionItemCreate
){

    const response = await API.post(
        "/collection-items/",
        data
    );
    

    return response.data
}



export async function deleteCollectionItem(
    itemId:number
){

    const response = await API.delete(
        `/collection-items/${itemId}`
    );


    return response.data;

}



export async function updateCollectionItem(
    itemId:number,
    data:CollectionItemUpdate
){

    const response = await API.put(
        `/collection-items/${itemId}`,
        data
    );


    return response.data;

}