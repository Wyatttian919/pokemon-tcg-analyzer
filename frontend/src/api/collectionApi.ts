import api from "./axios";
import type {

    CollectionItem,

    CollectionItemCreate,

    CollectionItemUpdate

} from "../types/collection";



export async function getUserCollection(
    userId:number
):Promise<CollectionItem[]> {


    const response = await api.get(
        `/users/${userId}/collection`
    );


    return response.data;

}



export async function addToCollection(
    data:CollectionItemCreate
){

    const response = await api.post(
        "/collection-items/",
        data
    );
    

    return response.data
}



export async function deleteCollectionItem(
    itemId:number
){

    const response = await api.delete(
        `/collection-items/${itemId}`
    );


    return response.data;

}



export async function updateCollectionItem(
    itemId:number,
    data:CollectionItemUpdate
){

    const response = await api.put(
        `/collection-items/${itemId}`,
        data
    );


    return response.data;

}