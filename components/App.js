import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Table from "./Table";
import Gestion from "./Gestion";
import store from "../store";
import { Provider } from "react-redux";
import {loadProveedores, loadDeltas, loadGestiones} from "../actionCreators";


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
            <Gestion/>
            

        </div>
      );
    }

  

    

  }




store.dispatch(loadProveedores())

store.dispatch(loadDeltas())
store.dispatch(loadGestiones())

ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('app')
    );
