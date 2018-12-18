import React from "react";
import { connect } from 'react-redux';
import store from "../store";

const divStyle = {
    height: '12px',

  };

const AgregaProveedor = ({proveedores,carteras,negocios,selectcartera,guarda}) =>{

      return (

          <div>


 
                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#exampleModal">
                Agrega 
                </button>

                <div style={divStyle}></div>

       
                <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Agregar Proveedor / Cartera / Score</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                        </button>
                    </div>

                    <form onSubmit={guarda}>
                            <div class="modal-body">
                            <label>Proveedores</label>
                            <select className='form-control' required={true} name='proveedor' onChange={(e)=>selectcartera(e)}>

                            <option></option>                    
                            {proveedores.map(item => (

                                <option  value={item.id} >{item.nombre}</option>

                            ))}
                                        
                            </select> 
                            
                            <div style={divStyle}></div>
                            <label>Carteras</label>
                            <select className='form-control' required={true} name='cartera' onChange={(e)=>selectcartera(e)}>

                            <option></option>                         
                            {carteras.map(item => (

                                <option  value={item.id} >{item.nombre}</option>

                            ))}
                                        
                            </select> 

                            <div style={divStyle}></div>
                            <label>Negocios</label>
                            <select className='form-control' required={true} name='negocio' onChange={(e)=>selectcartera(e)}>

                            <option></option>                         
                            {negocios.map(item => (

                                <option  value={item.id} >{item.nombre}</option>

                            ))}
                                        
                            </select> 

                            


                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                                <button type="submit" class="btn btn-primary"  >Guardar</button>
                            </div>

                    </form>
                    </div>
                    
                    
                </div>
                </div>
          </div>

          
       
      );


    }

const  mapStateToProps = state =>{


    console.log(state)

    return{
        proveedores:state.proveedores,
        carteras:state.carteras,
        negocios:state.negocios
        
    }

}






export default connect(mapStateToProps)(AgregaProveedor);