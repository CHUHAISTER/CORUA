import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";

const PageStat = () => {
  const location = useLocation();
  const { state } = location;
  const { data, puuid, matches } = state || {};

  const sortedMatches = Object.entries(matches).sort(([matchA, usersA], [matchB, usersB]) => {
    const userA = usersA.find((user) => user.puuid === puuid);
    const userB = usersB.find((user) => user.puuid === puuid);

    if (userA && !userB) {
      return -1;
    } else if (!userA && userB) {
      return 1;
    } else {
      return 0;
    }
  });


  return (
    <div class={"container"} >
      {sortedMatches.map(([match, users]) => (

          <div >
          {users.sort((a, b) => {
            if (a.puuid === puuid) {
              return -1;
            } else if (b.puuid === puuid) {
              return 1;
            } else {
              return 0;
            }
          }).map((user, index) => {
            const cardListWithQuantity = user.card_list.map(([card, quantity]) => ({
              card,
              quantity
            }));

            const cardTypes = cardListWithQuantity.reduce(
              (types, card) => {
                const type = card.card.type;
                const supertype = card.card.supertype;

                if (!types[type]) {
                  types[type] = [];
                }

                if (type === 'Unit' && supertype === 'Champion') {
                  if (!types['champion']) {
                    types['champion'] = [];
                  }
                  types['champion'].push(card);
                } else {
                  types[type].push(card);
                }

                return types;
              },
              {}
            );
            Object.values(cardTypes).forEach(cards => {
              cards.sort((a, b) => a.card.cost - b.card.cost);
            });

            return (
              <div key={index}>
                <h3>
                  {user.puuid === puuid && "Гра №" + (parseInt(match)+1)}
                </h3>
                <p>Puuid: {user.puuid}</p>
                <h3>{ user.puuid === puuid? data : "Enemy"}</h3>
<h2 style={{ color: "red" }}>
  {user.puuid === puuid && user.game_outcome && "Result: " + user.game_outcome}
</h2>


                <p style={{fontStyle:"italic"}}>Deck Code: {user.deck_code}</p>
                <p>Factions: {user.factions.join(", ")}</p>
                <p>Карти:</p>

                {Object.entries(cardTypes).map(([type, cards]) => (
                  <div key={type} className="row">
                    <h4>{type.charAt(0).toUpperCase() + type.slice(1) + "s"}:</h4>
                    <ul className="column-gap-0">
  {cards.map((card, index) => (
      <li key={index}>
  <div className="m-17kka91 d-flex align-items-center justify-content-between"
  style={{
    height: "100px",
    background: `linear-gradient(90deg, rgb(180, 86, 58) 20%, rgba(180, 86, 58, 0) 70%), url(${card.card.assets[0].fullAbsolutePath}) right center no-repeat`
  }}
>
  <div className="m-1a5qaex order-1">
    {card.card.cost}
  </div>
  <div className="m-toipa6 order-2">
    {card.card.name}
  </div>
  <div className="m-4g0zad order-3">
    {card.quantity}
  </div>
</div>
</li>





  ))}
</ul>

                  </div>
                ))}


              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
};

export default PageStat;
