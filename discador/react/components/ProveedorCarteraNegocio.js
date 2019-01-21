import React from "react";


import { connect } from 'react-redux';




const ProveedorCarteraNegocio = ({proveedor_cartera_negocio}) =>{

      return (

      
        <div>

             <h3>#{proveedor_cartera_negocio.length}</h3>
           
             <div className='row'>

                <div class='col-md-3'> <h3> Proveedor </h3></div>
                <div class='col-md-3'> <h3> Cartera </h3></div>
                <div class='col-md-3'> <h3> Negocio </h3></div>
                

            </div>

          

          <ul class="list-group">


            {proveedor_cartera_negocio.map(item=>
            
            <li class="list-group-item">
                
            <div className='row'>

                <div class='col-md-3'> {item.proveedor.nombre}  </div>
                <div class='col-md-3'> {item.cartera.nombre}  </div>
                <div class='col-md-3'> {
                    
                    item.negocio ? item.negocio.nombre : 'No tiene'
                    
                    
                    } 
                            
                </div>

                <div class='col-md-3'><a class='btn btn-sm btn-primary' href={'/discador/opcion_asigna_score/' + item.proveedor.id+'/'+item.cartera.id+'/'+item.negocio.id }>SCORE</a></div>


            </div>
            

            </li>



            )}
            

          </ul>


          </div>

          
       
      );


    }

const  mapStateToProps = state =>{


    console.log(state)

    return{

        proveedor_cartera_negocio:state.proveedor_cartera_negocio

    }

}




export default connect(mapStateToProps)(ProveedorCarteraNegocio);