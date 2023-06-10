import React from "react";
import { useLocation } from "react-router-dom";

const PageStat = () => {
  const location = useLocation();
  const { data = null, maths = null } = location.state || {};

  return (
    <div>
      <p>This is the stat page</p>
      <p>{data}</p>
        <p>{maths}</p>

    </div>
  );
};

export default PageStat;
