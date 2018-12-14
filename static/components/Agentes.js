
import React from "react";
import ReactDOM from "react-dom";

import Header from "./Header";
import { trae_cuentas, loadScore} from "../actionCreators";
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


      
        axios.get("/discador/api_cuentas")
        .then(response=>{

          console.log('trae_Cuenta',response.data)
    

          store.dispatch(trae_cuentas(response.data))
          
     

        });

        axios.get("/discador/api_detalle_cuentas/1")
        .then(response=>{

  
          this.setState({
            detalle_cuentas:response.data
          })

         

        });

    
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

        <Historial_agente detalle_cuentas={detalle_cuentas}/>
       

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



