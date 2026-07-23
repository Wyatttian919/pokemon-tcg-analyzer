import { useState } from "react";



interface SearchBarProps {

    onSearch:(keyword:string)=>void;

}



function SearchBar(
    {
        onSearch
    }:SearchBarProps
){


    const [keyword,setKeyword] = useState("");



    function handleSearch(){

        onSearch(keyword);

    }



    return (

        <div className="search-bar">


            <input

                value={keyword}

                onChange={
                    e =>
                    setKeyword(
                        e.target.value
                    )
                }

                placeholder="Search card name"

            />


            <button

                className="button"

                onClick={handleSearch}

            >

                Search

            </button>


        </div>

    );

}


export default SearchBar;