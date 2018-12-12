import React from "react";
import { loadCuentas } from "../actionCreators";
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Cuentas = ({cuentas,deltas}) =>{

      return (

          <ul class="list-group">
          <div class="form-group col-md-4">
              <select>

              
            {cuentas.map(product=>
            <option>{product.cliente}</option>
          
           

            )}
            
            </select>
</div>
          </ul>
       
      );


    }

const  mapStateToProps = state =>{

    return{
        cuentas:state.cuentas,
        deltas:state.deltas
    }

}






export default connect(mapStateToProps)(Cuentas);   