import { createStore,applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';

const cart = (state=[],action) => {

    if(action.type==='ADD_TO_CART'){
        return state.concat(action.product)
    }


    return state;

}

const proveedores = (state=[],action) => {

if(action.type==='PROVEEDORES'){
    return action.proveedores;
}
 return state;


 
}


const trae_carteras_proveedor = (state=[],action) => {

    if(action.type==='TRAE_CARTERAS_PROVEEDOR'){
        return action.trae_carteras_proveedor;
    }
     return state;
    
    
     
    }




const id_gestiones = (state=[],action) => {

    if(action.type==='TRAE_ID_GESTIONES'){

        console.log('INGRESE TRAE_ID_GESTIONES')

        return action.id_gestiones;
    }
        return state;
    
}



const resultados = (state=[],action) => {

    if(action.type==='TRAE_DATOS_RESULTADOS'){

        return action.resultados;
    }
        return state;
    
}

const subresultados = (state=[],action) => {

    if(action.type==='TRAE_DATOS_SUBRESULTADOS'){

        return action.subresultados;
    }
        return state;
    
}

        
const total_carteras = (state=[],action) => {


    if(action.type==='TOTAL_CONTADOR'){
        return action.total_carteras;
    }

    return state;
}
    


const gestiones = (state=[],action) => {

    if(action.type==='TRAE_GESTIONES'){
        return action.gestiones;
    }
    return state;
    
}



const score = (state=[],action) => {

    if(action.type==='TRAE_SCORE'){
        return action.score;
    }
    return state;

}


const cuentas = (state=[],action) => {

    if(action.type==='TRAE_CUENTITAS'){
        return action.cuentas;
    }
    return state;

}

const detalle_cuentass = (state=[],action) => {

    if(action.type==='TRAE_DETALLE_C'){
        return action.detalle_cuentas;
    } 
    return state;

}


const logger = store => next => action => {
    console.log('dispatching', action)
    let result = next(action)
    console.log('next state', store.getState())
    return result
  }




export default createStore(combineReducers({cart,proveedores,gestiones,total_carteras,cuentas,score,trae_carteras_proveedor,id_gestiones,resultados,subresultados,detalle_cuentass}),applyMiddleware(logger,thunk));

