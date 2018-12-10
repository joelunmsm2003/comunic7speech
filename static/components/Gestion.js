import React from "react";
import { connect } from 'react-redux';
import { loadProveedores } from "../actionCreators"


const Gestion = ({gestiones}) =>{

      return (
        <div className='row'>
            <h1>Gestiones</h1>
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



export default connect(mapStateToProps)(Gestion);