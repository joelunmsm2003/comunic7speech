import React from "react";
import ReactDOM from "react-dom";
import Table from "./Table";

class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            value: "",
            editar:[]
        };

    
      }

    render() {
      return (
        <div>
            <h1>Hola</h1>
            <Table/>

        </div>
      );
    }
  }



ReactDOM.render(
    <App />,
    document.getElementById('app')
    );
