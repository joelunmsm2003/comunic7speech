import React from "react";


import { loadProveedores } from "../actionCreators"
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Proveedores = ({proveedores,deltas}) =>{

      return (

          <ul class="list-group">
             
            {proveedores.map(product=>
            
            <li class="list-group-item">{product.nombre}</li>

            )}

          </ul>
       
      );


    }

const  mapStateToProps = state =>{

    return{
        proveedores:state.proveedores,
        deltas:state.deltas
    }

}



export default connect(mapStateToProps)(Proveedores);