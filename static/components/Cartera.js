import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Header from "./Header";
import Gestion from "./Gestion";
import Select from "./Select";
import store from "../store";
import { Provider } from "react-redux";
import {loadProveedores, loadDeltas, loadGestiones,total_carteras} from "../actionCreators";
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
       
    
                     
         <Select/>
              
                

        
        </div>
      );
    }

  }

  



store.dispatch(loadProveedores())

store.dispatch(loadDeltas())
store.dispatch(loadGestiones())
store.dispatch(total_carteras())


ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('app')
    );
