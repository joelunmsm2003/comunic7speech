import React from "react";
import { connect } from 'react-redux';

const divStyle = {

    margin:'40px',
    position:'absolute',

    padding:'5px',
 
    bottom:'0',
    'z-index':'1000',
    right:'0'



}; 


const Alerta = ({mensaje}) =>{

      return (

       
         <div style={divStyle} className="alert alert-dark" role="alert">
           {mensaje ? mensaje : 'No tiene'}
            </div>
          
         
       
      );


    }



const  mapStateToProps = state =>{

   console.log(state)

    return{
       
    }

}


export default connect(mapStateToProps)(Alerta);   