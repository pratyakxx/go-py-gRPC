import React from "react";


const Status = ({connected}) => {

    return(
        <div>{connected ?
            <div className="connecttrue">
                CONNECTED
            </div>
            :
            <div className="connectfalse">
                DISCONNECTED
            </div>
            }
        </div>
    )
}
export default Status;

