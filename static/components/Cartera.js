import React from "react";
import ReactDOM from "react-dom";

import Header from "./Header";
import ProveedorCartera from "./ProveedorCartera";
import store from "../store";
import { Provider } from "react-redux";
import axios from 'axios';


class App extends React.Component {
    constructor(props) {

        console.log('carteras..')

        super(props);

        this.state = {
            value: "",
            editar:[],
            cart:[],
            carteras:[],
            proveedor:[]
        };
    
      }


      componentDidMount() {

      



        axios.get("/discador/api_carteras_proveedor/"+window.location.href.split('/')[5])
        .then(response=>{


          this.setState({
            carteras: response.data,
            proveedor:response.data[0]['proveedor']
  
          });
            


        });



     

      }

    render() {

      const { carteras,proveedor } = this.state;

      return (
        <div> 
         <Header/>

         <div class='container'>              

          <h1>Proveedor {proveedor.nombre}</h1>    
         
         <ProveedorCartera carteras={carteras}/>

         </div>

        </div>
      );
    }

}




  





ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('app')
    );
