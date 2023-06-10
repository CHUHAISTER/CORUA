import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import PageStat from "./PageStat";
const HomePage = () => {
  const [inputValue, setInputValue] = useState("");
    const [inputTag, setInputTag] = useState("");

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
  if (data.message) {
    console.log(data.message);
    navigate('/stat', { state: { data: data.message, maths: data.maths } });
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
    </div>
  );
};

export default HomePage;
