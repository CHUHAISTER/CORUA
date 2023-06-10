import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import PageStat from "./PageStat";
const HomePage = () => {
  const [inputValue, setInputValue] = useState("");
    const [inputTag, setInputTag] = useState("");
  const [errorHome, setErrorHome] = useState("");
    const navigate  = useNavigate();

  const handleSubmit = () => {
    const data = {
    inputValue: inputValue,
      inputTag: inputTag,
  };

  // Send the data to the backend using fetch
  fetch('http://127.0.0.1:8000/api/find_account', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
.then(data => {
  if (data.matches) {
    console.log(data.message);
    navigate('/stat', { state: { data: inputValue, matches: data.matches } });
  }
  else if (data.error) {
      console.log('Error:', data.error);
      setErrorHome(data.error);
  } else {
      console.log('Error: Message field not found in response');
    }
})

  };

  return (
    <div>
      <p>This is the home page</p>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />
      <input
        type="text"
        value={inputTag}
        onChange={(e) => setInputTag(e.target.value)}
      />
      <button onClick={handleSubmit}>Submit</button>
      <p>{errorHome}</p>
        <img src='http://dd.b.pvp.net/4_5_0/core/en_us/img/regions/icon-freljord.png'></img>
    </div>
  );
};

export default HomePage;
