import React from "react";

import { addToCart } from "../actionCreators"
import { connect } from 'react-redux';


const Table = ({cart,addToCart}) =>{

      return (
        <div className='row'>

            {cart.map(product=>
            <li>{product}</li>
            
            )}

            <div className='col-md-3'>
            <a onClick={()=>addToCart('00')}>Ingresar</a>
            </div>
  
        </div>
      );


    }



    


const  mapStateToProps = state =>{

    return{
        cart:state.cart
    }

}

const mapDispatchToProps = dispatch=>{
    return{

        addToCart(data){

            console.log(data)
      
            dispatch(addToCart(data))
            
        }

    }

}


export default connect(mapStateToProps,mapDispatchToProps)(Table);