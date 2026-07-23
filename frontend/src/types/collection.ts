export interface CollectionItem {

    id:number;
    quantity:number;
    condition:string;
    purchase_price?:number;

    card:{

        id:number;
        name:string;
        number:string;
        image_url:string;

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