import React from "react";
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Historial_agente = ({detalle_cuentas}) =>{

      return (

         <div>
           
           <h1></h1>

           <ul class="list-group">
                <div class="form-group col-md-12">
                    <h3>Historial de Gestión</h3>
               
                    <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">Id</th>
                           
                          </tr>
                        </thead>  

                      <tbody>
                      {detalle_cuentas.map(product=>
                              <tr>
                                <td>{product.id}</td>
                                
                              
                              </tr>
                      )}
                      </tbody>
                      </table>
                  </div>
            </ul> 

          </div>
       
      );


    }



const  mapStateToProps = state =>{

   console.log(state)

    return{

      detalle_cuentas:state.detalle_cuentas
        
    }

}


export default connect(mapStateToProps)(Historial_agente);   