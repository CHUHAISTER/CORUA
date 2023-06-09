import React, {Component} from "react";
import {render} from "react-dom";
import HomePage from "./HomePage";
import PageStat from "./PageStat";

export default class App extends Component{
    constructor(props) {
        super(props);
    }

    render()
    {
        return (<div>
            <HomePage/>
            <PageStat/>
            </div>);
    }
}
const appDiv = document.getElementById("app");
render(<App/>, appDiv);