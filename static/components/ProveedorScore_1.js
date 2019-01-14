import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Header from "./Header";
import Gestion from "./Gestion";
import Cuentas from "./Cuentas";
import Alerta from "./Alerta";
import AsignaScore from "./AsignaScore"
import store from "../store";
import { Provider } from "react-redux";
import {cargaproveedores,total_carteras,proveedores, loadCarteras,loadNegocios, loadGestiones} from "../actionCreators";
import AppRouter from "./Rutas"
import axios from 'axios';
import AgregaProveedor from "./AgregaProveedor";
var $ = require ('jquery')

const divStyle = {
  height: '12px',

};

class ProveedorScore extends React.Component {
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


     buscascore(data){

      console.log('buscascore',data)
     }

     onTextChange(data) {

      
       
          const name_select = data.target.name+'_name';
          const name = data.target.name;
          const value = data.target.value
          const select_option = data.target.options[event.target.selectedIndex].text

          this.setState({
            [name]: value,
            [name_select]: select_option
          });


          if (name=='negocio'){

            console.log('entre')

            axios.get("/discador/api_resultados_negocio/"+value)
                  .then(response=>{


                    this.setState({
                      score_negocios: response.data,
                      
                    });  

        
              });

            }

  
 
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

      const { mensaje,proveedor,proveedor_name,cartera_name,negocio_name,score_negocios } = this.state;

      return (

        <div>

            <Header/>

            
            <div style={divStyle}></div>

            <div class='container'>

              
                <h4>Asignacion del Score</h4>

              
                { mensaje ? <Alerta mensaje={mensaje}/> : <div></div>}
                

                <AgregaProveedor guarda={this.handleSubmit.bind(this)}  selectcartera={this.onTextChange.bind(this)}/>

                <div style={divStyle}></div>

                <h3>{negocio_name}</h3>

              
                <AsignaScore score_negocios={score_negocios} activascore={(e,item)=>this.activascore(e,item)} buscascore={(e,item)=>this.buscascore(item)}/>


    
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
    <ProveedorScore />
    </Provider>,
    document.getElementById('app')
    );
