import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Header from "./Header";
import Gestion from "./Gestion";
import Cuentas from "./Cuentas";
import store from "../store";
import { Provider } from "react-redux";
import {loadProveedores, loadDeltas, loadGestiones,total_carteras,loadCuentas} from "../actionCreators";
import AppRouter from "./Rutas"

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
       
            <div class='container'>
           
              
              
                <Proveedores/>
                <Gestion/>
                <Cuentas/>
              
                

            </div>
        </div>
      );
    }

  }

  
store.dispatch(loadProveedores())

store.dispatch(loadDeltas())
store.dispatch(loadGestiones())
store.dispatch(total_carteras())
store.dispatch(loadCuentas())

ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('app')
    );
