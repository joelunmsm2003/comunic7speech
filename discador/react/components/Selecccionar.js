import React from "react";
import { connect , trae_telefonos} from 'react-redux';


const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const Seleccionar = ({trae_telefonos}) =>{

      return (

         <div>
           
           <h1></h1>

           <ul class="list-group">
                <div class="form-group col-md-12">
                    <h3>Teléfonos</h3>
               
                    <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">numero telefonico</th>
                           
                          </tr>
                        </thead>  

                      <tbody>
                      {trae_telefonos.map(product=>
                              <tr>
                                <td>{product.id}</td>
                                
                              
                              </tr>
                      )}
                      </tbody>
                      </table>
                  </div>
            </ul> 

          </div>
       
      );


    }



const  mapStateToProps = state =>{

   console.log(state)

    return{
        trae_telefonos:state.trae_telefonos
    }

}


export default connect(mapStateToProps)(Seleccionar);   