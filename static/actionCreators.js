import axios from 'axios';

const loadProveedores = ()=>{

    return dispatch =>{

         return axios.get("http://localhost:8000/discador/api_proveedor")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_PROVEEDORES",
                proveedores:response.data
            })
        });
    };

  

}

const loadGestiones = ()=>{

    return dispatch =>{

         return axios.get("http://localhost:8000/discador/api_gestiones")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_GESTIONES",
                gestiones:response.data
            })
        });
    };

  

}

const loadDeltas = ()=>{

    return dispatch =>{

         return axios.get("http://localhost:8000/discador/api_proveedor")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_DELTAS",
                deltas:response.data
            })
        });
    };


    
  

}


const loadCarteras = ()=>{

    return dispatch =>{

         return axios.get("http://localhost:8000/discador/api_carteras")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_CARTERAS",
                carteras:response.data
            })
        });
    };

}



 const loadCuentas = ()=>{

        return dispatch =>{
    
             return axios.get("http://localhost:8000/discador/api_cuentas")
            .then(response=>{
                console.log(response)
                dispatch({
                    type:"TRAE_CUENTAS",
                    cuentas:response.data
                })
            });
        };
}
const addToCart = producto => {

    return {

        type:"ADD_TO_CART",
        product:producto

      }
}


export { addToCart,loadProveedores,loadDeltas,loadGestiones,loadCarteras,loadCuentas };