
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
            <form>
                       
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

<div class="form-group row"> 
<div class="tab-content" id="myTabContent">
  <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">



    <div class="form-group row">
    <label for="staticEmail" class="col-sm-1 col-form-label">DNI:</label>
    <div class="col-sm-2">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="75417613"></input>
    </div>
    <label for="staticEmail" class="col-sm-2 col-form-label">Nombre Completo:</label>
    <div class="col-sm-3">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="Daniel Acevedo Ruiz"></input>
    </div>

    <label for="staticEmail" class="col-sm-2 col-form-label">Fecha/Nac</label>
    <div class="col-sm-2">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value=" 27-03-79"></input>
    </div>
  </div>

<form>
  <div class="form-group row">
    <label for="staticEmail" class="col-sm-2 col-form-label">DEPARTAMENTO:</label>
    <div class="col-sm-2">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="LIMA"></input>
    </div>
    <label for="staticEmail" class="col-sm-2 col-form-label">PROVINCIA :</label>
    <div class="col-sm-2">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value=" LIMA"></input>
    </div>

    <label for="staticEmail" class="col-sm-2 col-form-label">DISTRITO :</label>
    <div class="col-sm-2">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="MIRAFLORES"></input>
    </div>
  </div>
</form>
  </div>
  
  <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
  <form>
  <div class="form-group row">
    <label for="staticEmail" class="col-sm-1 col-form-label">Email</label>
    <div class="col-sm-2">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="email@example.com"></input>
    </div>
    <label for="staticEmail" class="col-sm-1 col-form-label">Email</label>
    <div class="col-sm-2">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="email@example.com"></input>
    </div>
  </div>
  
</form>
      
      
  </div>
  <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">...</div>
  <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">...</div>
  <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">...</div>
 
</div>
</div>
</form>

<form>
  <div class="form-group row">
    <label for="staticEmail" class="col-sm-1 col-form-label">Email</label>
    <div class="col-sm-2">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="email@example.com"></input>
    </div>
    <label for="staticEmail" class="col-sm-1 col-form-label">Email</label>
    <div class="col-sm-2">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="email@example.com"></input>
    </div>
  </div>
  
</form>
               
                <Cuentas/>
                
               
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



