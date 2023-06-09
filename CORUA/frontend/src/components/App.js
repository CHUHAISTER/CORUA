import React, {Component} from "react";
import {render} from "react-dom";
import HomePage from "./HomePage";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  Redirect,
} from "react-router-dom";
import PageStat from "./PageStat";

const App = () =>{
    return(
        <Router>
            <Routes>
                <Route path="/" element = {<HomePage/>}/>
                <Route path="/stat" element={<PageStat/>} />
            </Routes>
        </Router>
    );
}
render(<App/>, document.getElementById("app"));