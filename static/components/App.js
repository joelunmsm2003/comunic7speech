import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Header from "./Header";
import Gestion from "./Gestion";
import Cuentas from "./Cuentas";
import Alerta from "./Alerta";
import AsignaScore from "./AsignaScore";
import Carteras from "./AsignaScore"
import store from "../store";
import { Provider } from "react-redux";
import {proveedor_cartera_negocio,cargaproveedores,total_carteras,proveedores, loadCarteras,loadNegocios, loadGestiones} from "../actionCreators";
import AppRouter from "./Rutas"
import axios from 'axios';
import AgregaProveedor from "./AgregaProveedor";
import ProveedorCarteraNegocio from "./ProveedorCarteraNegocio";
import AgregaProveedorCarteraNegocio from "./AgregaProveedorCarteraNegocio";
var $ = require ('jquery')

const divStyle = {
  height: '12px',

};

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
            negocio_name:"",
            score_negocios:[],
            mensaje:""



        };

    
      }

      componentDidMount() {


        store.dispatch(loadCarteras())

        store.dispatch(loadNegocios())

        store.dispatch(proveedor_cartera_negocio())

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


      activascore(data,item){


        console.log(item.gestion)


        this.setState({

          mensaje:data.target.options[event.target.selectedIndex].text+' '+item.gestion.nombre

        })


      




        this.setState({

          mensaje:""
        })
  


        axios.post('/discador/api_asigna_score/', {
          item,
          estado:data.target.value,
          proveedor:{
          proveedor_id:this.state.proveedor,
          cartera_id:this.state.cartera,
          negocio_id:this.state.negocio}
        })
        .then(function (response) {
  
          
        
        })
        .catch(function (error) {
          console.log(error);
        });



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


          console.log(data.target.name,data.target.value)

      
          const name = data.target.name;
          const value = data.target.value

          this.setState({
            [name]: value
          });

    }


    

    handleSubmit(data){


      axios.post('/discador/guardaproveedor/', {
        proveedor_id: this.state.proveedor,
        cartera_id:this.state.cartera,
        negocio_id:this.state.negocio
      })
      .then(function (response) {

        window.location.reload()

      })
      .catch(function (error) {
        console.log(error);
      });

      data.preventDefault()
    

    }

    render() {

      const { carteras,mensaje,proveedor,proveedor_name,cartera_name,negocio_name,score_negocios } = this.state;

      return (

        <div>

            <Header/>

            
            <div style={divStyle}></div>

            <div class='container'>


                <h5>Asigne una cartera/negocio a su Proveedor</h5>

                { mensaje ? <Alerta mensaje={mensaje}/> : <div></div>}
                

                <AgregaProveedorCarteraNegocio guarda={this.handleSubmit.bind(this)}  selectcartera={this.onTextChange.bind(this)}/>

                <div style={divStyle}></div>


                 <ProveedorCarteraNegocio/>


              


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
