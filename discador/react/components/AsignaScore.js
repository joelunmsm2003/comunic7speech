import React from "react";
import { connect } from 'react-redux';

const divStyle = {

    margin: '40px',
    border: '5px solid pink'

};



const AsignaScore = ({score_negocios,activascore,buscascore}) =>{

      return (

         <div>
           

                   <input value={this.item}  onChange={(e)=>buscascore(e,this.item)} />

                    <table class="table">
                        <thead>
                            <tr>
                            <th scope="col">Tipo de Gestion</th>
                            <th scope="col">ID Gestion</th>
                            <th scope="col">Resultado</th>
                            <th scope="col">Justificación</th>

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
                                            <select className='form-control' onChange={(e)=>activascore(e,item)}>
                                                <option value='1'>Desactivar</option>
                                                <option value='2'>Activar</option>
                                            </select>
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
        
    }

}


export default connect(mapStateToProps)(AsignaScore);   