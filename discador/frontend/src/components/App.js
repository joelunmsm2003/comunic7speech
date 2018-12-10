import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Table from "./Table";
import store from "../store";
import { Provider } from "react-redux";
import {loadProveedores, loadDeltas} from "../actionCreators";


class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            value: "",
            editar:[],
            cart:[]
        };
    
      }

    render() {
      return (
        <div>
            <h1>Hola</h1>
            <Table/>
            <Proveedores/>
            

        </div>
      );
    }

  

    

  }


store.dispatch(loadProveedores())
store.dispatch(loadDeltas())

ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('app')
    );
