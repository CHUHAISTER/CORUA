import React from "react";


export const PageStat = (props) =>{
    const {
  data = null
} = props.location?.state || {};

    return (<div>
            <p>This is the stat page</p>
            <p>{data}</p>
    </div>
        );

}
export default PageStat;