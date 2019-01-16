import React from "react";
import { connect } from 'react-redux';
import { trae_id_gestion,trae_resultados,trae_subresultados } from "../actionCreators"
import store from "../store";




const Select = ({data,gestiones,id_gestiones,resultados,subresultados,id_proveedor}) =>{

      return (

        <div>
            {id_proveedor}
        <div className='form-row'>
                <div className='form-group col-md-3'>

                        <label for="cartera">Carteras</label>
                        <select id='cartera' className='form-control'>
                                                            
                        {data.map(item => (

                            <option  value={item.id} >{item.cartera.nombre}</option>

                        ))}

                        </select>
                </div> 

                <div className='form-group col-md-3'>
                    <label>Gestiones</label>
                    <select className='form-control' onChange={(e)=>store.dispatch(trae_id_gestion(e.target.value))} >
                                                        
                        {gestiones.map(item => (

                            <option  value={item.id} >{item.nombre}</option>

                        ))}

                    </select> 


                </div>



                <div className='form-group col-md-3'>
                    <label>IDGestiones</label>
                    <select className='form-control'  onChange={(e)=>store.dispatch(trae_resultados(e.target.value))}  >

                        {id_gestiones ?
                                                        
                        id_gestiones.map(item => (

                            <option  value={item.id} >{item.nombre}</option>

                        )):

                        <option></option>

                        }

                    </select> 


                </div>


                <div className='form-group col-md-3'>
                    <label>Resultados</label>
                    <select className='form-control' onChange={(e)=>store.dispatch(trae_subresultados(e.target.value))} >

                        {resultados ?
                                                        
                        resultados.map(item => (

                            <option  value={item.id} >{item.nombre}</option>

                        )):

                        <option></option>

                        }

                    </select> 


                </div>




                
        </div>
            
                <h1>Justificacion</h1>
                <ul class="list-group">
                        
                        {subresultados ?
                        
                         subresultados.map(item=>

                            <div className='col-md-3'>
                                <li class="list-group-item">
                                    <div className='row'>
                                    <div className='col-md-6'>
                                    {item.nombre}</div>
                                    <div className='col-md-6'><input type='checkbox'/></div>
                                    </div>
                                </li>
                            </div>
                        ):
                        
                        <li>No existe datos</li>
                        
                        }

                </ul>

        </div>
      );

}


const  mapStateToProps = state =>{

    console.log('mapStateToProps',state)

    return{
        data:state.trae_carteras_proveedor,
        gestiones:state.gestiones,
        id_gestiones:state.id_gestiones,
        resultados:state.resultados,
        subresultados:state.subresultados
    }

}





export default connect(mapStateToProps)(Select);