import axios from 'axios';

export const cargaproveedores = (data,total)=>{


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







export const trae_resultados = (data)=>{


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

export const trae_subresultados = (data)=>{


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

export const trae_carteras_proveedor = (data)=>{


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

export  const trae_id_gestion = (data)=>{


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










export const loadGestiones = ()=>{

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



export const loadCarteras = ()=>{

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

export const loadNegocios = ()=>{

    return dispatch =>{

         return axios.get("/discador/api_negocios")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_NEGOCIOS",
                negocios:response.data
            })
        });
    };

}


export const loadCuentas = ()=>{

        return dispatch =>{
    
             return axios.get("/discador/api_cuentas")
            .then(response=>{
                console.log(response)
                dispatch({
                    type:"TRAE_CUENTAS",
                    cuentas:response.data
                })
            });
        };

}

export const loadScore = ()=>{

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

export const trae_cuentas = data=>{

    console.log('ARMA..... HAHAHAHHA',data)


        return dispatch =>{

             dispatch({
                 type:"TRAE_CUENTITAS",
                 cuentas:data
             })
        
        };


}



export const detalle_cuentas = ()=>{

    return dispatch =>{

         return axios.get("/discador/api_detalle_cuentas/1")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_DETALLE_CUENTAS",
                detalle_cuentas:response.data
            })
        });
    };
}

export const proveedores = ()=>{

    return dispatch =>{

         return axios.get("/discador/api_proveedor/")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"PROVEEDORES",
                proveedores:response.data
            })
        });
    };
}







