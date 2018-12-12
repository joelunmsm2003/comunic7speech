import React from "react";
import { connect } from 'react-redux';
import { loadProveedores } from "../actionCreators"


const Select = ({gestiones}) =>{

      return (
        <div className='container'>
            <h1>Carteras</h1>
            {gestiones.map(data=>
            <li>{data.nombre}</li>
            
            )}
        </div>
      );

}


const  mapStateToProps = state =>{

    return{
        gestiones:state.gestiones,
    }

}



export default connect(mapStateToProps)(Select);