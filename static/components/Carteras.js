import React from "react";
import { loadCarteras } from "../actionCreators";
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Carteras = ({carteras}) =>{

      return (

          <ul class="list-group">
          <div class="form-group col-md-4">
              <select>

              
            {carteras.map(product=>
            <option>{product.nombre}</option>
          
           

            )}
            
            </select>
            </div>
          </ul>
       
      );


    }

const  mapStateToProps = state =>{

    return{
    }

}






export default connect(mapStateToProps)(Carteras);   