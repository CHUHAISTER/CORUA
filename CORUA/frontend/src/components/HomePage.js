import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import PageStat from "./PageStat";

const HomePage = () => {
  const [inputValue, setInputValue] = useState("");
  const [inputValue2, setInputValue2] = useState("");
  const [inputTag, setInputTag] = useState("");
  const [errorHome, setErrorHome] = useState("");
  const navigate = useNavigate();

  const handleSubmit = () => {
    const data = {
      inputValue: inputValue,
      inputTag: inputTag,
    };

    // Send the data to the backend using fetch
    fetch("http://127.0.0.1:8000/api/find_account", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.matches) {
          console.log(data.puuid);
          navigate("/stat", {
            state: { data: inputValue, puuid: data.puuid, matches: data.matches },
          });
        } else if (data.error) {
          console.log("Error:", data.error);
          setErrorHome(data.error);
        } else {
          console.log("Error: Message field not found in response");
        }
      });
  };

  const handleInputChange = (e) => {
    setInputValue2(e.target.value);
    setInputTag(e.target.value);
  };

  return (
    <div className="container d-flex flex-column align-items-center justify-content-center vh-100">
      <h1 className="mb-4">Вітаю, друже! Ми вже на тебе зачекались</h1>
      <div className="mb-3">
        <input
          type="text"
          className="form-control"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="ім'я в ЛОР"
        />
      </div>
      <div className="mb-3">
        <select
          className="form-select"
          value={inputValue2}
          onChange={handleInputChange}
        >
          <option value="">Вибери свій тег</option>
          <option value="EUNE">EUNE</option>
          <option value="EUW">EUW</option>
          <option value="custom">Custom</option>
        </select>
      </div>
      {inputValue2 === "custom" && (
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            value={inputTag}
            onChange={(e) => setInputTag(e.target.value)}
            placeholder="Custom value"
          />
        </div>
      )}
      <button className="btn btn-primary" onClick={handleSubmit}>Submit</button>
<p className="text-danger fs-5  fw-bold">{errorHome}</p>
    </div>
  );
};

export default HomePage;
