import React from "react";
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Historial_agente = ({detalle_cuentas}) =>{

      return (

         <div>
           
           <h1>Cuentas</h1>

           <ul class="list-group">
                <div class="form-group col-md-6">
                    <h3>Informacion de Cuentas</h3>
               
                    <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">Nº Cuenta</th>
                            <th scope="col">Dias/Mora</th>
                            <th scope="col">Total</th>
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
        
    }

}


export default connect(mapStateToProps)(Historial_agente);   