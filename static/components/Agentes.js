
import React from "react";
import ReactDOM from "react-dom";

import Header from "./Header";
import { trae_cuentas, loadScore,detalle_cuentas} from "../actionCreators";
import Tabs from "./Tabs";
import Cuentas from "./Cuentas";
import Historial_agente from "./Historial_agente";

import Score from "./Score";
import store from "../store";
import { Provider } from "react-redux";
import axios from "axios"


class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
          detalle_cuentas:[{id:1}]

        };

  
      }


      componentDidMount() {

        store.dispatch(detalle_cuentas())
    
      }

    render() {

      
      const {detalle_cuentas} = this.state

      return (

        <div>
        <Header/>
        <div class='container'>
        

        <Tabs/>
        
        <Cuentas/>

        <Score/>

        <Historial_agente/>
       

        </div>
        </div>

      );
    }

  }

  // store.dispatch(total_carteras())
  store.dispatch(loadScore())
 



ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('root')
    );



