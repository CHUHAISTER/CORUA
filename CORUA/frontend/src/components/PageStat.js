import React from "react";
import { useLocation } from "react-router-dom";

const PageStat = () => {
  const location = useLocation();
  const { data = null, matches = null } = location.state || {};

  return (
    <div>
      <p>This is the stat page</p>
      <p>Name: {data}</p>

        {matches && Object.keys(matches).map((key) => (
          <p key={key}>Match {key}: {JSON.stringify(matches[key])}</p>
        ))}

    </div>
  );
};


export default PageStat;
