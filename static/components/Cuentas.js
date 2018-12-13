import React from "react";
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Cuentas = ({cuentas}) =>{

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
                      {cuentas.map(product=>
                              <tr>
                                <td>{product.numero_cuenta}</td>
                                <td>{product.mora}</td>
                                <td>{product.total}</td>
                              
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
        cuentas:state.cuentas
    }

}


export default connect(mapStateToProps)(Cuentas);   