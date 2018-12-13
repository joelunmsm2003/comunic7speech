import axios from 'axios';

const loadProveedores = ()=>{

    return dispatch =>{

         return axios.get("/discador/api_proveedor")
        .then(response=>{
            

            this.contador=0

            for (this.i = 0; this.i < response.data.length; this.i++) { 
                

                this.contador++
            }

            console.log(',,,,,',response.data)

            dispatch({
                type:"TRAE_PROVEEDORES",
                proveedores:response.data,
                contador:this.contador
            })
        });
    };


}


const total_carteras = ()=>{

    return dispatch =>{

        return axios.get("/discador/api_proveedor")
       .then(response=>{
  
           this.contador=0

           for (this.i = 0; this.i < response.data.length; this.i++) { 
               console.log('hahah',response.data[this.i].contar_carteras)

               this.contador=this.contador+response.data[this.i].contar_carteras
           }


           dispatch({
               type:"TOTAL_CONTADOR",
               total_carteras:this.contador,
               
           })
       });
   };


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

const loadDeltas = (data)=>{


    console.log('Ingrese a deltas.........',data)

    return dispatch =>{

         return axios.get("/discador/api_proveedor")
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
                    type:"TRAE_CUENTAS",
                    cuentas:response.data
                })
            });
        };
}

const loadScore = ()=>{

    return dispatch =>{

         return axios.get("http://localhost:8000/discador/api_score")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_SCORE",
                score:response.data
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



export { addToCart,loadProveedores,loadDeltas,loadGestiones,total_carteras,loadCarteras,loadCuentas,loadScore,trae_carteras_proveedor,trae_id_gestion,trae_resultados,trae_subresultados };
