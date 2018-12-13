import React from "react";
import { loadCuentas } from "../actionCreators";
import { loadDCuentas } from "../actionCreators";

import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Cuentas = ({cuentas,deltas}) =>{

      return (

          <ul class="list-group">
          <div class="form-group col-md-4">
          <h3>Informacion de Cuentas</h3>
          <br></br>
          <table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Nº Cuenta</th>
      <th scope="col">Dias/Mora</th>
      <th scope="col">Total</th>
    </tr>
  </thead>  

           
            {cuentas.map(product=>

   
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>{product.numero_cuenta}</td>
      <td>{product.dias_mora}</td>
      <td>{product.total}</td>
    </tr>
    
  </tbody>

            )}
            </table>
              
          
</div>


          </ul>
       
      );


    }

const DCuentas = ({dcuentas,deltas}) =>{

      return (

          <ul class="list-group">
          <div class="form-group col-md-4">
          <h3>Informacion de Cuentas</h3>
          <br></br>
          <table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Nº Cuenta</th>
      <th scope="col">Dias/Mora</th>
      <th scope="col">Total</th>
    </tr>
  </thead>  

           
{dcuentas.map(product=>

   
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>{product.id}</td>
      <td>{product.nombre}</td>
      
    </tr>
    
  </tbody>

            )}
            </table>
              
          
</div>
          </ul>
       
      );


    }

const  mapStateToProps = state =>{

    return{
        cuentas:state.cuentas,
        dcuentas:state.dcuentas,
        deltas:state.deltas
    }

}






export default connect(mapStateToProps)(Cuentas,DCuentas);   