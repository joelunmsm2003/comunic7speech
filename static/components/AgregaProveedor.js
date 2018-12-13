import React from "react";
import { connect } from 'react-redux';


const divStyle = {
    height: '12px',

  };

const AgregaProveedor = ({}) =>{

      return (

          <div>

              <button className='btn btn-light'>Agrega Proveedor</button>

              <div style={divStyle}></div>
          </div>

          
       
      );


    }

const  mapStateToProps = state =>{


    console.log(state)

    return{
        proveedores:[],
    }

}






export default connect(mapStateToProps)(AgregaProveedor);