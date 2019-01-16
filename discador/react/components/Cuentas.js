import React from "react";
import { connect , trae_cuentas} from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Cuentas = ({trae_cuentas}) =>{

      return (

         <div>
           
           <h1></h1>

           <ul class="list-group">
                <div class="form-group col-md-12">
                    <h3>Información de Cuentas</h3>
               
                    <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">Nº Cuenta</th>
                            <th scope="col">Dias/Mora</th>
                            <th scope="col">Total</th>
                          </tr>
                        </thead>  

                      <tbody>
                      {trae_cuentas.map(product=>
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
        trae_cuentas:state.trae_cuentas
    }

}


export default connect(mapStateToProps)(Cuentas);   