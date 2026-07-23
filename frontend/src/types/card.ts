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