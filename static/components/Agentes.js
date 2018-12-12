
import React from "react";
import ReactDOM from "react-dom";
import Proveedores from "./Proveedores";
import Header from "./Header";
import Score from "./Score";
import Gestion from "./Gestion";
import Cuentas from "./Cuentas";
import store from "../store";
import { Provider } from "react-redux";
import {loadProveedores, loadDeltas, loadGestiones,total_carteras,loadCuentas,loadScore} from "../actionCreators";
import AppRouter from "./Rutas"

class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            value: "",
            editar:[],
            cart:[]
        };
    
      }

    render() {
      return (

        <div>
       
            <div class='container'>
              
            <ul class="nav nav-tabs" id="myTab" role="tablist">
  <li class="nav-item">
    <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Clientes</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile" aria-selected="false">Telefonos</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact" aria-selected="false">Direcciones</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact" aria-selected="false">Contacto</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact" aria-selected="false">Email</a>
  </li>
</ul>
<div class="tab-content" id="myTabContent">
  <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
      <li>DNI</li>
      <li>DEPARTAMENTO</li>
  </div>
  <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
      <li>NUMERO</li>
  </div>
  <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">...</div>
  <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">...</div>
  <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">...</div>
</div>
               
                <Cuentas/>
                
                <Gestion/>
                <Score/>
              
                

            </div>


        </div>
      );
    }

  }

  
store.dispatch(loadProveedores())

store.dispatch(loadDeltas())
store.dispatch(loadGestiones())
store.dispatch(total_carteras())
store.dispatch(loadCuentas())
store.dispatch(loadScore())

ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('root')
    );



