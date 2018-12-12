import React from "react";
import { loadScore } from "../actionCreators";
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};

const Score = ({score,deltas}) =>{

      return (

          <ul class="list-group">
          <div class="form-group col-md-4">
            Resultados Dela Gestion
          <br></br>
              <select>

        
{score.map(product=>
            <option>{product.gestion.nombre}</option>
            
            )}
            
            </select>



</div>
          </ul>


       
      );

    


    }





const  mapStateToProps = state =>{

    return{
        score:state.score,
        deltas:state.deltas
    }

}

export default connect(mapStateToProps)(Score);   