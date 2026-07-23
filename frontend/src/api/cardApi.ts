import api from "./axios";
import type {
    CardSearchResult,
    CardDetail
} from "../types/card";




export async function searchCards(
    name: string
): Promise<CardSearchResult[]> {

    const response = await api.get(
        "/cards/search",
        {
            params: {
                name
            }
        }
    );


    return response.data;
}



export async function getCardDetail(
    id:number
):Promise<CardDetail>{


    const response = await api.get(
        `/cards/${id}`
    );


    return response.data;

}