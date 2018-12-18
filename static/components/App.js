import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Header from "./Header";
import Gestion from "./Gestion";
import Cuentas from "./Cuentas";
import store from "../store";
import { Provider } from "react-redux";
import {cargaproveedores,total_carteras,proveedores, loadCarteras,loadNegocios, loadGestiones} from "../actionCreators";
import AppRouter from "./Rutas"
import axios from 'axios';
import AgregaProveedor from "./AgregaProveedor";
var $ = require ('jquery')


class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            value: "",
            editar:[],
            carteras:[],
            proveedor:"",
            cartera:"",
            negocio:"",
            proveedor_name:"",
            cartera_name:"",
            negocio_name:""



        };

    
      }

      componentDidMount() {


        store.dispatch(loadCarteras())

        store.dispatch(loadNegocios())

        //store.dispatch(proveedores())


        this.listaproveedores()

        
      }


      listaproveedores(){
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

     onTextChange(data) {

      
          console.log('selec.ss..',data.target.options[event.target.selectedIndex].text)

          const name_select = data.target.name+'_name';
          const name = data.target.name;
          const value = data.target.value
          const select_option = data.target.options[event.target.selectedIndex].text

          this.setState({
            [name]: value,
            [name_select]: select_option
          });

  
 
    }


    

    handleSubmit(data){


      axios.post('/discador/guardaproveedor/', {
        proveedor_id: this.state.proveedor,
        cartera_id:this.state.cartera
      })
      .then(function (response) {

        $('.modal-backdrop').hide(); // for black background
        $('body').removeClass('modal-open'); // For scroll run
        $('#exampleModal').modal('hide'); 

      })
      .catch(function (error) {
        console.log(error);
      });

      data.preventDefault()
    

    }

    render() {

      const { proveedor,proveedor_name } = this.state;

      return (

        <div>

            <Header/>

            
       
            <div class='container'>

              
                {proveedor_name}

                <AgregaProveedor guarda={this.handleSubmit.bind(this)}  selectcartera={this.onTextChange.bind(this)}/>
    
                <input type='text' onChange={this.busca_proveedor.bind(this)} className='form-control' placeholder='Buscar Proveedor'></input>
                

                {proveedor_name.proveedor ? proveedor_name.proveedor.nombre : '' } 


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
