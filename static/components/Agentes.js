
import React from "react";
import ReactDOM from "react-dom";

import Header from "./Header";
import { trae_cuentas } from "../actionCreators";
import Tabs from "./Tabs";
import Cuentas from "./Cuentas";
import store from "../store";
import { Provider } from "react-redux";
import axios from "axios"


class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

        };
    
      }


      componentDidMount() {


      
        axios.get("/discador/api_cuentas")
        .then(response=>{

          console.log(response.data)
    

          store.dispatch(trae_cuentas(response.data))
     

        });

        

       
      }

    render() {
      return (

        <div>
        <Header/>
        <div class='container'>
        

        <Tabs/>
        <Cuentas/>




        </div>
        </div>

      );
    }

  }

  



ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('root')
    );



