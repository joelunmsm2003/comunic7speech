import React from "react";

import { loadProveedores } from "../actionCreators"
import { connect } from 'react-redux';


const Proveedores = ({proveedores,deltas}) =>{

      return (
        <div className='row'>
            <h1>Proveedores</h1>
            {proveedores.map(product=>
            <li>{product.nombre}</li>
            
            )}

            <h1>Deltas</h1>

            {deltas.map(product=>
            <li>{product.nombre}</li>
            
            )}

           
        </div>
      );


    }



    
const  mapStateToProps = state =>{

    return{
        proveedores:state.proveedores,
        deltas:state.deltas
    }

}



export default connect(mapStateToProps)(Proveedores);