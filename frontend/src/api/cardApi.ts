import axios from "axios";


const API = axios.create({
    baseURL: "http://localhost:8000"
});


export interface CardSearchResult {
    id: number;
    name: string;
    number: string;
    rarity?: string;
    image_url?: string;
}


export interface CardDetail {

    id:number;

    pokemon_api_id:string;

    name:string;

    number:string;

    rarity?:string;

    category?:string;

    card_type?:string;

    hp?:number;

    image_url?:string;


    set:{
        id:number;
        name:string;
    };

}


export async function searchCards(
    name: string
): Promise<CardSearchResult[]> {

    const response = await API.get(
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


    const response = await API.get(
        `/cards/${id}`
    );


    return response.data;

}