import React from "react";


const Header = ()=> {

      return (

          <nav class="navbar navbar-expand-lg navbar-light bg-light">

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
                
                <a class="navbar-brand" href="#">Comunica7</a>
                <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                <li class="nav-item active">
                  
                   
                <div class="btn-group">
                <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Administrador
                </button>
                <div class="dropdown-menu">
                    <a class="dropdown-item" href="/discador/opcion_proveedor">Score</a>
                    
                    <a class="dropdown-item" href="/discador/agentes">Agente</a>
                    <a class="dropdown-item" href="#">Something else here</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Separated link</a>
                </div>
                </div>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Marcador</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Importador</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Salir</a>
                </li>
                </ul>
                
            </div>


          </nav>


       
      );


    }

export default Header;