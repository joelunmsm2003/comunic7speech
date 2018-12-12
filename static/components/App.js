import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Header from "./Header";
import Gestion from "./Gestion";
import Cuentas from "./Cuentas";
import store from "../store";
import { Provider } from "react-redux";
import {loadProveedores, loadDeltas, loadGestiones,loadCuentas} from "../actionCreators";



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
        <Header/>
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
store.dispatch(loadCuentas())

ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('app')
    );
