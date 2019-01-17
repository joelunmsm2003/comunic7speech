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
import axios from 'axios';

var $ = require ('jquery')

const espacio = {
  height: '12px',

};

class ProveedorScore extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
       
          proveedores:[],
          proveedor:"",
          carteras:[],
          muestraproveedor:false,
          muestracartera:false,
          negocios:[],
          muestracartera:false,
          gestiones:[],
          gestion:false,
          muestragestiones:false,
          negocio:false,
          resultados:[],
          cartera:false,
          muestranegocio:false,
          muestraresultado:false,
          scores:[]

        };

    
      }

      componentDidMount() {

        axios.get("/discador/api_proveedor")
        .then(response=>{
    
          this.setState({

          proveedores:response.data
           
          })
    
        });


        axios.get("/discador/api_gestiones")
        .then(response=>{

          console.log('gestiones',response.data)
    
          this.setState({

          gestiones:response.data
           
          })
    
        });


        axios.get("/discador/api_resultados")
        .then(response=>{

    
          this.setState({

          resultados:response.data
           
          })
    
        });




        
      }


      seleccionaproveedor(e,data){

        this.setState({
          proveedor:data
        })
  
        axios.get("/discador/api_carteras_proveedor/"+data.id)
        .then(response=>{
    
          this.setState({
            carteras:response.data,
            muestraproveedor:false,
            muestracartera:false,
            negocios:[],
            cartera:false
           
          })
    
        });




      }

      seleccionacartera(e,proveedor,cartera){


        console.log(proveedor,cartera)

        this.setState({

          cartera:cartera,
          muestracartera:false

         
        
        })


        
  
        axios.get("/discador/api_carteras_negocios/"+proveedor.id+'/'+cartera.cartera.id)
        .then(response=>{
    
          this.setState({
            negocios:response.data
         
          })
    
        });



        


      }


      seleccionanegocio(e,negocio){



        this.setState({

          negocio:negocio,
         

        })


      }

      showproveedor(){

        this.setState({

          muestraproveedor:true
           
          })

      }

      showcartera(){

        this.setState({

          muestracartera:true
           
          })

      }

      showgestion(){

        this.setState({

          muestragestiones:true
           
          })

      }

      showresultado(){

        this.setState({

          muestraresultado:true
           
          })

      }

      seleccionagestion(e,data){




        this.setState({

          gestion:data,
          muestragestiones:false,
          resultado:false
          
           
          })


          
        
      }


      seleccionaresultado(e,data){


        console.log(data)


        this.setState({

          resultado:data,
          muestraresultado:false
          
           
          })
        
      }


      buscar(){

        console.log('data...')

        let currentComponent = this;

        axios.post('/discador/api_busca_score/', {
      
          data:this.state,
          
        })
        .then(function (response) {


          console.log(response.data)

          currentComponent.setState({

            scores:response.data

          })
  
          
        
        })
        .catch(function (error) {
          console.log(error);
        });
        
      }

      


    
     

          
        
      
    

    render() {

      const {scores,muestraresultado,resultados,resultado,muestragestiones,proveedores,carteras,cartera,muestraproveedor,muestracartera,proveedor,negocios,gestiones,gestion,negocio} = this.state;

      let todo =''
      let todocartera
      let todogestiones=''
      let todoresultados=''
      let todoscores=''
      let botones=''

      const sinestilo = "list-group-item d-flex justify-content-between align-items-center"

      const conestilo = "list-group-item d-flex justify-content-between align-items-center list-group-item-primary"

      if(muestraproveedor){

        todo=proveedores.map(item=>
            
          <li className= {item.contar_carteras>0 ? sinestilo : conestilo} onClick={(e) => this.seleccionaproveedor(e,item)}>
            
            
            {item.nombre}
            
            <span class="badge badge-primary badge-pill">{item.contar_carteras}</span>
            </li>

          )

         

      }
      else{

       todo= <li class="list-group-item list-group-item-action"  onClick={(e) => this.showproveedor(e)} >{proveedor ? proveedor.nombre : 'Selecciona proveedor' }</li>

      }



                
        
              


     


      if(muestracartera){

        todocartera = carteras.map(item=>

                  <li class="list-group-item list-group-item-action"  onClick={(e) => this.seleccionacartera(e,proveedor,item)}>{item.cartera.nombre}</li>

                  )

      }
      else{


        todocartera=<li class="list-group-item list-group-item-action" onClick={(e) => this.showcartera(e)}  >{cartera ? cartera.cartera.nombre : 'Selecciona cartera' }</li>

      }

      if(muestragestiones){

        todogestiones = 
      
          gestiones.map(item=>
            
          <li className= "list-group-item" onClick={(e) => this.seleccionagestion(e,item)} >
            
    
            {item.nombre}
            
            </li>

          )
        }

        else{


          todogestiones = <li className= "list-group-item" onClick={(e) => this.showgestion(e)}>{gestion ? gestion.nombre : 'Seleccione gestion'}     
          </li>
        }


        if(muestraresultado){

          todoresultados =  resultados.map(item=>
            
            <li className= "list-group-item" onClick={(e) => this.seleccionaresultado(e,item)} >
              
      
              {item.nombre}
              
              </li>
  
            )

        }

        else{

          todoresultados = <li className= "list-group-item" onClick={(e) => this.showresultado(e)}>{resultado ? resultado.nombre : 'Seleccione resultado'}     
          </li>

        }

        

          console.log('entres a ascore...')

 

      return (

        <div>

             

            <Header/>

            


            <div class='container'>

            <h1>Score</h1>

            <div class='row'>

            <div class='col-md-4'>


               

                <div class="list-group">
                
                <h6>Proveedores</h6>
                {todo}

                </div>
 

            </div>
            <div class='col-md-4'>

                  <div class="list-group">

                    <h6>Carteras</h6>
                    {todocartera}


                    </div>

            </div>
            <div class='col-md-4'>

                <h6>Negocios</h6>
                {negocios.map(item=>


                <li class="list-group-item list-group-item-action"  onClick={(e) => this.seleccionanegocio(e,item)}>{item.negocio.nombre}</li>

                )}
                </div>





            </div>

              <div style={espacio}></div>
            <div class='row'>

                <div class='col-md-4'>


                      
                      <h6>Gestiones</h6>
                      {todogestiones}

                     

                </div>


                <div class='col-md-4'>
                  
                  <h6>Resultados</h6>
                  {todoresultados}</div>


            </div>

            
            <div style={espacio}></div>

            <button class='btn btn-primary' onClick={(e) => this.buscar(e)}>Buscar</button>

            <div style={espacio}></div>
            
            <table class='table'>

            <thead class="thead-dark">
              <tr>
                <th scope="col">Gestion</th>
                <th scope="col">Resultado</th>
                <th scope="col">Justificacion</th>
               
              </tr>
            </thead>

            <tbody>
            {scores.map(item=>
            <tr>

              <td>
              

              {item.gestion.nombre}
              
              </td>
              <td>
              

              {item.resultado.nombre}
              
              </td>
            <td>
              

              {item.subresultado.nombre}
              
              </td>
            </tr>

            )}

            </tbody>
            </table>

            
            
            
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
