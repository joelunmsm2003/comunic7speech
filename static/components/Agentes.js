
import React from "react";
import ReactDOM from "react-dom";

import Header from "./Header";
import { trae_cuentas, loadScore,detalle_cuentas,trae_telefonos} from "../actionCreators";
import Tabs from "./Tabs";
import Cuentas from "./Cuentas";
import Historial_agente from "./Historial_agente";

import Score from "./Score";
import store from "../store";
import Telefonos from "./Telefonos";
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
       
        <div class="form-group row">
        
              <div class="form-group col-md-6">
              <div class="card" >
                        
          <Cuentas/>
                       
              </div>
          </div>
          <div class="form-group col-md-6">
          <div class="card" >
         <Historial_agente/>
        
         </div>
         </div>


         <div class="form-group col-md-6">
        <div class="card" >
        <Score/>
        </div>
        </div>




<div class="form-group col-md-6">
<div class="card" >
        <Telefonos/>
       
        </div>  
        </div> 
       
        </div>



        </div>
        </div>

      );
    }

  }

  // store.dispatch(total_carteras())
  store.dispatch(loadScore())
  store.dispatch(trae_cuentas())
  store.dispatch(trae_telefonos())
 
 



ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('root')
    );



