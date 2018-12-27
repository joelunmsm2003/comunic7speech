import React from "react";


import { connect } from 'react-redux';




const ProveedorCartera = ({carteras}) =>{

      return (

      
        <div>

             <h3>#{carteras.length}</h3>
           
             <div className='row'>

                <div class='col-md-3'> <h3> Cartera </h3></div>
                <div class='col-md-3'> <h3> Negocio </h3></div>
                

            </div>

          

          <ul class="list-group">


            {carteras.map(item=>
            
            <li class="list-group-item">
                
            <div className='row'>

                <div class='col-md-3'> {item.cartera.nombre}  </div>
                <div class='col-md-3'> {
                    
                    item.negocio ? item.negocio.nombre : 'No tiene'
                    
                    
                    } 
                            
                </div>


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

    }

}




export default connect(mapStateToProps)(ProveedorCartera);