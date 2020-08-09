import React from "react";


const Details = ({data}) => {

    return(
        <div className="details">
            <p>Name: {data.name}</p>
            <p>Code : {data.alpha2Code}</p>
            <p>Capital :{data.capital}</p>
            <p>Population :{data.population}</p>
            <p>SubRegion: {data.subregion}</p>
        </div>
    )
}
export default Details;

