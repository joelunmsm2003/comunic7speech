import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Header from "./Header";
import Gestion from "./Gestion";
import Cuentas from "./Cuentas";
import store from "../store";
import { Provider } from "react-redux";
import {cargaproveedores,total_carteras} from "../actionCreators";
import AppRouter from "./Rutas"
import axios from 'axios';
import AgregaProveedor from "./AgregaProveedor";



class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            value: "",
            editar:[],
            cart:[],
            proveedores:[]
        };
    
      }

      componentDidMount() {


        console.log('entre aca.....')

        axios.get("/discador/api_proveedor")
        .then(response=>{
    
          console.log(response.data)

          this.setState({
            proveedores:response.data,
            filterproveedores:response.data
          })

          

          this.contador = this.contador_carteras(response.data)


          store.dispatch(cargaproveedores(response.data,this.contador))


    
        });


        
      }

      contador_carteras(data){

          this.contador=0

          for (this.i = 0; this.i < data.length; this.i++) { 

            this.contador=this.contador+data[this.i].contar_carteras

          }

          return this.contador

      }



     busca_proveedor(data){

          this.state.filterproveedores = this.state.proveedores.filter((poet) => {

            let poetName = poet.nombre
          
            return poetName.indexOf(
              data.target.value) !== -1
          })

          this.contador = this.contador_carteras(this.state.filterproveedores)

          store.dispatch(cargaproveedores(this.state.filterproveedores,this.contador))

          

     }

    render() {
      return (

        <div>

            <Header/>

            
       
            <div class='container'>


                <AgregaProveedor/>
    
                <input type='text' onChange={this.busca_proveedor.bind(this)} className='form-control' placeholder='Buscar Proveedor'></input>
                

                <Proveedores/>

             
              

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
