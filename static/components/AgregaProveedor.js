import React from "react";
import { connect } from 'react-redux';
import store from "../store";

const divStyle = {
    height: '12px',

  };

const AgregaProveedor = ({proveedores,carteras,negocios,selectcartera,guarda}) =>{

      return (

          <div>



                <div style={divStyle}></div>

                    <form onSubmit={guarda}>


                            <div class='row'>


                                    <div className='col-md-3'>
                          
                                        <label>Proveedores</label>
                                        <select className='form-control' required={true} name='proveedor' onChange={(e)=>selectcartera(e)}>

                                        <option></option>                    
                                        {proveedores.map(item => (

                                            <option  value={item.id} >{item.nombre}</option>

                                        ))}
                                                    
                                        </select> 

                                    </div>
                            
                                    <div className='col-md-3'>

                                        <label>Carteras</label>
                                        <select className='form-control' required={true} name='cartera' onChange={(e)=>selectcartera(e)}>

                                        <option></option>                         
                                        {carteras.map(item => (

                                            <option  value={item.id} >{item.nombre}</option>

                                        ))}
                                                    
                                        </select> 
                                    
                                    </div>

                                    <div className='col-md-3'>

                                        <label>Negocios</label>
                                        <select className='form-control' required={true} name='negocio' onChange={(e)=>selectcartera(e)}>

                                        <option></option>                         
                                        {negocios.map(item => (

                                            <option  value={item.id} >{item.nombre}</option>

                                        ))}
                                                    
                                        </select> 

                                    </div>

                            </div>

                    </form>
                    
                    
                    
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