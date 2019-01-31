import React from "react";
import ReactDOM from "react-dom";
import Header from "./Header";

import axios from 'axios';

class App extends React.Component { 

  constructor(props) {
    super(props);

    this.state = {
   
      proveedores:[],
      proveedor:'',
      carteras:[],
      negocios:[],
      cartera:'',
      gestiones:[],
      resultados:[]


    };


  }

  componentDidMount() {

    axios.get("/discador/api_proveedor")
    .then(response=>{

      this.setState({

      proveedores:response.data,
      carteras:[]
       
      })

    });


    axios.get("/discador/api_gestiones")
    .then(response=>{

      
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

  seleccionaproveedor(e){


    console.log(e.target.value)

    this.setState({
      proveedor:e.target.value
    })

    axios.get("/discador/api_carteras_proveedor/"+e.target.value)
    .then(response=>{

      this.setState({
        carteras:response.data,

       
      })

    });




  }


  seleccionacartera(e,proveedor){


    console.log('seleccionacartera',proveedor)

    this.setState({

      cartera:e.target.value,

    
    })


    

    axios.get("/discador/api_carteras_negocios/"+proveedor+'/'+e.target.value)
    .then(response=>{

      this.setState({
        negocios:response.data
     
      })

    });


  }


  seleccionanegocio(e,cartera){



    this.setState({

      negocio:e.target.value


    })

  }

  render() { 

    const {proveedores,carteras,proveedor,negocios,cartera,gestiones,resultados} = this.state;

      return (


        <div>
          <Header/>

          <div className='container'>

            <div class='row'>

            <div class='col-md-4'>
          <label>Proveedor</label>
          <select class='form-control' onChange={(e) => this.seleccionaproveedor(e)}>
          <option>Seleccionar</option>
          {proveedores.map(item=>


            <option value={item.id}>{item.nombre}</option>
            )}
            </select>

            </div>

            <div class='col-md-4'>

            <label>Cartera</label>
            <select class='form-control' onChange={(e) => this.seleccionacartera(e,proveedor)}>

              <option>Seleccionar</option>
          {carteras ? carteras.map(item=>


            <option value={item.cartera.id}>{item.cartera.nombre}</option>
            ) : <option></option>}
            </select>

            </div>

            <div class='col-md-4'>

            <label>Negocios</label>
            <select class='form-control' onChange={(e) => this.seleccionanegocio(e,cartera)}>

          <option>Seleccionar</option>
          {negocios ? negocios.map(item=>

            
            <option value={item.id}>{item.negocio.nombre}</option>
            ) : <option></option>}
            </select>

            </div>

            </div>


             <div class='row'>

                      <div class='col-md-4'>

                        <label>Gestion</label>
                        <select class='form-control' onChange={(e) => this.seleccionanegocio(e,cartera)}>

                        <option>Seleccionar</option>
                        {gestiones ? gestiones.map(item=>


                        <option value={item.id}>{item.nombre}</option>
                        ) : <option></option>}
                        </select>


                      </div>


                      <div class='col-md-4'>

                        <label>Resultados</label>
                        <select class='form-control' onChange={(e) => this.seleccionaresultado(e,cartera)}>

                        <option>Seleccionar</option>
                        {resultados ? resultados.map(item=>


                        <option value={item.id}>{item.nombre}</option>
                        ) : <option></option>}
                        </select>


                      </div>


             </div>




          </div>

          </div>

      )
          
       
  } 
} 

ReactDOM.render(<App />, document.getElementById('app'));