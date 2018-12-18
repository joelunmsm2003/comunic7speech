import React from "react";
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const AsignaScore = ({score_negocios}) =>{

      return (

         <div>
           

                   

                    <table class="table">
                        <thead>
                            <tr>
                            <th scope="col">Gestion</th>
                            <th scope="col">IDGestion</th>
                            <th scope="col">Resultado</th>
                            <th scope="col">SubResultado</th>

                            </tr>
                        </thead>  

                        <tbody>

                          

                            {score_negocios ?
                                score_negocios.map(item=>
                                            <tr>
                                          
                                            <td>{item.gestion.nombre}</td>
                                            
                                            <td>{ item.idgestion ? item.idgestion.nombre: 'No existe'}</td>
                                            <td>{ item.resultado ? item.resultado.nombre: 'No existe'}</td>
                                            <td>{ item.subresultado ? item.resultado.nombre: 'No existe'}</td>
                                            <td>
                                            <label class="switch">
                                            <input type="checkbox" defaultChecked/>
                                            <span class="slider round"></span>
                                            </label>
                                            </td>


                                            <td></td>
                                            </tr>
                                    )
                                    :'No hay Registros'                           
                            }
                        </tbody>
                      </table>

                      
                      
                    



          </div>
       
      );


    }



const  mapStateToProps = state =>{

   console.log('00000',state)

    return{
        score_negocios:state.score_negocios
    }

}


export default connect(mapStateToProps)(AsignaScore);   