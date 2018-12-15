import axios from 'axios';

const cargaproveedores = (data,total)=>{


    return dispatch =>{

        dispatch({
            type:"PROVEEDORES",
            proveedores:data,
            
        })

        dispatch({
            type:"TOTAL_CONTADOR",
            total_carteras:total,
            
        })

    }
 
}






const trae_resultados = (data)=>{


    console.log(data)


    return dispatch =>{


        return axios.get("/discador/api_resultados/"+data)
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_DATOS_RESULTADOS",
                resultados:response.data,
            })
        });
 

    }

}

const trae_subresultados = (data)=>{


    console.log(data)


    return dispatch =>{


        return axios.get("/discador/api_subresultados/"+data)
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_DATOS_SUBRESULTADOS",
                subresultados:response.data,
            })
        });
 

    }

}

const trae_carteras_proveedor = (data)=>{


    return dispatch =>{


        return axios.get("/discador/api_carteras_proveedor/"+data)
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_CARTERAS_PROVEEDOR",
                trae_carteras_proveedor:response.data,
            })
        });
 

    }

}

 const trae_id_gestion = (data)=>{


    console.log('actioncreator....',data)


     return dispatch =>{


         return axios.get("/discador/api_id_gestion/"+data)
         .then(response=>{
             console.log('APIIIIIIIIII')
             dispatch({
                 type:"TRAE_ID_GESTIONES",
                 id_gestiones:response.data,
             })
         });
 

     }

 }










const loadGestiones = ()=>{

    return dispatch =>{


         return axios.get("/discador/api_gestiones")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_GESTIONES",
                gestiones:response.data
            })
        });


    };

  

}



const loadCarteras = ()=>{

    return dispatch =>{

         return axios.get("/discador/api_carteras")
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
    
             return axios.get("/discador/api_cuentas")
            .then(response=>{
                console.log(response)
                dispatch({
                    type:"TRAE_DETALLE_CUENTAS",
                    cuentas:response.data
                })
            });
        };

}

const loadScore = ()=>{

    return dispatch =>{

         return axios.get("/discador/api_score")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_DATOS_SCORE",
                score:response.data
            })
        });
    };
}





// const loadDCuentas2 = ()=>{

//     return dispatch =>{

//          return axios.get("http://localhost:8000/discador/api_detalle_cuentas/3")
//         .then(response=>{
//             console.log(response)
//             dispatch({
//                 type:"TRAE_DETALLE_CUENTAS",
//                 score:response.data
//             })
//         });
//     };
// }


// const loadCuentas = ()=>{

//     return dispatch =>{

//          return axios.get("/discador/api_cuentas")
//         .then(response=>{
//             console.log(response)
//             dispatch({
//                 type:"TRAE_DETALLE_CUENTAS",
//                 cuentas:response.data
//             })
//         });
//     };

// }

const trae_cuentas = data=>{

    console.log('ARMA..... HAHAHAHHA',data)


        return dispatch =>{

             dispatch({
                 type:"TRAE_CUENTITAS",
                 cuentas:data
             })
        
        };


}




const addToCart = producto => {

    return {

        type:"ADD_TO_CART",
        product:producto

      }
}



export { trae_cuentas,addToCart,cargaproveedores,loadGestiones,total_carteras,loadCarteras,loadScore,trae_carteras_proveedor,trae_id_gestion,trae_resultados,trae_subresultados };
