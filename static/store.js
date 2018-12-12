import { createStore,applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';

const cart = (state=[],action) => {

    if(action.type==='ADD_TO_CART'){
        return state.concat(action.product)
    }


    return state;

}

const proveedores = (state=[],action) => {

if(action.type==='TRAE_PROVEEDORES'){
    return action.proveedores;
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

const deltas = (state=[],action) => {

    if(action.type==='TRAE_DELTAS'){
        return action.deltas;
    }
    return state;

}


const logger = store => next => action => {
    console.log('dispatching', action)
    let result = next(action)
    console.log('next state', store.getState())
    return result
  }

export default createStore(combineReducers({cart,proveedores,deltas,gestiones,total_carteras}),applyMiddleware(logger,thunk));