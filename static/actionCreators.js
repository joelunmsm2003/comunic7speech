import axios from 'axios';

const loadProveedores = ()=>{

    return dispatch =>{

         return axios.get("http://localhost:8000/discador/api_proveedor")
        .then(response=>{
            console.log('action response.....FOR')

            this.contador=0

            for (this.i = 0; this.i < response.data.length; this.i++) { 
                console.log('hahah',response.data[this.i])

                this.contador++
            }


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

        return axios.get("http://localhost:8000/discador/api_proveedor")
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
                    type:"TRAE_DETALLE_CUENTAS",
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


const loadDCuentas = ()=>{

    return dispatch =>{

         return axios.get("http://localhost:8000/discador/api_detalle_cuentas/3")
        .then(response=>{
            console.log(response)
            dispatch({
                type:"TRAE_DETALLE_CUENTAS",
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


export { addToCart,loadProveedores,loadDeltas,loadGestiones,total_carteras,loadCarteras,loadCuentas,loadScore,loadDCuentas };
