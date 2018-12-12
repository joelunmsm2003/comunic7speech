import React from "react";


import { loadProveedores } from "../actionCreators"
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Proveedores = ({proveedores,deltas,total_carteras}) =>{

      return (

      
                    

          <ul class="list-group">

                 <div className='row'>

                    <div class='col-md-3'> <h1>Proveedor </h1></div>
                    <div class='col-md-3'><h1>Industria</h1></div>
                    <div class='col-md-3'><h1># {total_carteras}</h1></div>

                </div>
             
            {proveedores.map(product=>
            
            <li class="list-group-item">
                
            <div className='row'>

                <div class='col-md-3'> {product.nombre}  </div>
                <div class='col-md-3'>
                            { 
                            product.industria ? product.industria.nombre : 'No tiene'
                            }
                </div>

                <div class='col-md-3'>
                           <a href={'/discador/carteras/' + product.id}>{product.contar_carteras}</a> 
                </div>



            </div>
            

            </li>


            )}

          </ul>

          
       
      );


    }

const  mapStateToProps = state =>{


    console.log(state)

    return{
        proveedores:state.proveedores,
        deltas:state.deltas,
        total_carteras:state.total_carteras
    }

}



export default connect(mapStateToProps)(Proveedores);