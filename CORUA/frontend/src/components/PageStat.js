import React from "react";
import { useLocation } from "react-router-dom";

const PageStat = () => {
  const location = useLocation();
  const { matches = [] } = location.state || {};

  return (
    <div style={{ height: '600px', overflowY: 'scroll' }}>
      {Object.entries(matches).map(([match, users]) => (
        <div key={match}>
          <h2>{match}</h2>
          {users.map((user, index) => (
            <div key={index}>
              <h3>User {index + 1}</h3>
              <p>Puuid: {user.puuid}</p>
              <p>Deck Code: {user.deck_code}</p>
              <p>Factions: {user.factions.join(", ")}</p>
              <p>Карти:</p>
              <ul>
                {user.card_list.map((card, index) => (
                  <li key={index}>
                    <img src={card[0].assets[0].gameAbsolutePath} alt={card[0].name} />
                    <div>Кількість: {card[1]}</div>
                  </li>
                ))}
              </ul>
              <h2 style={{color: "red"}}>Result: {user.game_outcome}</h2>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default PageStat;
