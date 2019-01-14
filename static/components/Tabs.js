import React from "react";
import { connect } from 'react-redux';




const Tabs = () =>{

      return (

         <div >
         < div className="container">
         <div class="card" >
            <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
                    <li class="nav-item">
                        <a class="nav-link active" id="pills-home-tab" data-toggle="pill" href="#pills-home" role="tab" aria-controls="pills-home" aria-selected="true">Clientes</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" id="pills-profile-tab" data-toggle="pill" href="#pills-profile" role="tab" aria-controls="pills-profile" aria-selected="false">Telefono</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" id="pills-contact-tab" data-toggle="pill" href="#pills-contact" role="tab" aria-controls="pills-contact" aria-selected="false">Direcciones</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" id="pills-m-tab" data-toggle="pill" href="#pills-m" role="tab" aria-controls="pills-m" aria-selected="false">Contactos</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link" id="pills-email-tab" data-toggle="pill" href="#pills-email" role="tab" aria-controls="pills-email" aria-selected="false">Email</a>
                    </li>
            </ul>
            </div>


            <div class="tab-content" id="pills-tabContent">
                <div class="tab-pane fade show active" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">1
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
                        <div class="form-group row">
                                <label for="staticEmail" class="col-sm-2 col-form-label">Departamento:</label>
                                <div class="col-sm-2">
                                <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="Lima"></input>
                                </div>
                                <label for="staticEmail" class="col-sm-2 col-form-label">Provincia :</label>
                                <div class="col-sm-2">
                                <input type="text" readonly class="form-control-plaintext" id="staticEmail" value=" Lima"></input>
                                </div>

                                <label for="staticEmail" class="col-sm-2 col-form-label">Distrito :</label>
                                <div class="col-sm-2">
                                <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="Miraflore"></input>
                                </div>
                        </div>
                
                </div>
                <div class="tab-pane fade" id="pills-profile" role="tabpanel" aria-labelledby="pills-profile-tab">.2.
                
                
                
                
                
                </div>
                <div class="tab-pane fade" id="pills-contact" role="tabpanel" aria-labelledby="pills-contact-tab">.3.</div>
                <div class="tab-pane fade" id="pills-m" role="tabpanel" aria-labelledby="pills-m-tab">.4.</div>
                <div class="tab-pane fade" id="pills-email" role="tabpanel" aria-labelledby="pills-email-tab">.5.</div>
            </div>

 <hr></hr>
 
</div>
          </div>
         
       
      );


    }



const  mapStateToProps = state =>{

   console.log(state)

    return{
        cuentas:state.cuentas
    }

}


export default connect(mapStateToProps)(Tabs);   