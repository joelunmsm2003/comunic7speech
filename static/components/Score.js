import React from "react";
import { loadScore} from "../actionCreators";
import { connect } from 'react-redux';


const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};

const Score = ({score}) =>{

      return (

          <ul class="list-group">
          <div class="form-group col-md-12">
            <h3>Resultados De la Gestión</h3>
          <br></br>
                    <div className="form-group"> 
                    <label for="exampleFormControlSelect1">Tipo de la Gestión</label>
                    <div class="form-group row">        
             <select class="form-control col-sm-6" id="exampleFormControlSelect1">

        
{score.map(product=>
            <option>{product.gestion.nombre}</option>
            
            )}
            
            </select>
                  
 <select class="form-control col-sm-6" id="exampleFormControlSelect1">
 
        
{score.map(product=>

            <option>{product.resultado.nombre}</option>
            
            )}
            
            </select>
            </div>
            </div>


<button type="button" class="btn btn-primary">Guardar</button>
</div>


          </ul>
      
      );

    }




const  mapStateToProps = state =>{

    return{
        score:state.score,
     
       
    }

}

export default connect(mapStateToProps)(Score);   