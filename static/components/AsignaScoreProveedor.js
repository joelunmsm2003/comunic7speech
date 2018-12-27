import React from "react";
import ReactDOM from "react-dom";

import Header from "./Header";
import ProveedorCartera from "./ProveedorCartera";
import store from "../store";
import { Provider } from "react-redux";
import axios from 'axios';
import AsignaScore from "./AsignaScore";


class AsignaScoreProveedor extends React.Component {
    constructor(props) {

        console.log('carteras..')

        super(props);

        this.state = {
            value: "",
            editar:[],
            cart:[],
            carteras:[],
            proveedor:[],
            scoreproveedores:[],
            proveedor_cartera_negocio:[]
        };
    
      }


      componentDidMount() {




        console.log(window.location.href.split('/'))

        this.pro = window.location.href.split('/')[5]
        this.car = window.location.href.split('/')[6]
        this.neg = window.location.href.split('/')[7]



        axios.get("/discador/api_detalle_proveedor_cartera_negocio/"+this.pro+'/'+this.car+'/'+this.neg)
        .then(response=>{


              console.log('data,,,,',response.data)

              this.setState({

                scoreproveedores:response.data,
                proveedor_cartera_negocio:response.data[0]

              })


        });



     

      }

    render() {

      const {scoreproveedores,proveedor_cartera_negocio} = this.state;

      return (
        <div> 
         <Header/>

         <div class='container'> 
           
                        

          <h3> {proveedor_cartera_negocio.proveedor ? proveedor_cartera_negocio.proveedor.nombre : 'No tiene'}</h3>
           <h4>  {proveedor_cartera_negocio.cartera ? proveedor_cartera_negocio.cartera.nombre : 'No tiene'}</h4>
           <h5>  {proveedor_cartera_negocio.negocio ? proveedor_cartera_negocio.negocio.nombre : 'No tiene'}</h5>  

          <AsignaScore score_negocios={scoreproveedores}/>
         

         </div>

        </div>
      );
    }

}




  





ReactDOM.render(

    <Provider store={store}>
    <AsignaScoreProveedor />
    </Provider>,
    document.getElementById('app')
    );
