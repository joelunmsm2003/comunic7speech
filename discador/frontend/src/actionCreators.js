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

const addToCart = producto => {

    return {

        type:"ADD_TO_CART",
        product:producto

      }
}


export { addToCart,loadProveedores,loadDeltas };