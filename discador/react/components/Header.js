
import React from "react";
import 'bootstrap';

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
              <button type="button" class="btn btn-light dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Mantenimiento
              </button>
              <div class="dropdown-menu">
                  <a class="dropdown-item" href="/discador/opcion_clientes">Clientes</a>
                  
                  <a class="dropdown-item" href="/discador/agentes">Provedores</a>
                  <a class="dropdown-item" href="/discador/opcion_score">Score</a>
                  <a class="dropdown-item" href="#">Usuarios</a>
                 
                  
    </div>
    </div>
    </li>

    <li class="nav-item active">
              
               
                    <div class="btn-group">
                    <button type="button" class="btn btn-light dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Procesos
                    </button>
                    <div class="dropdown-menu">
                        <a class="dropdown-item" href="/discador/opcion_proveedor">Panel General del Cliente</a>
                        
                        <a class="dropdown-item" href="/discador/agentes">Procesos Masivos de cuenta</a>
                        <a class="dropdown-item" href="#">Usuarios</a>
                        
                        
                    </div>
                    </div>
                    </li>


    <li class="nav-item active">
              
               
                        <div class="btn-group">
                        <button type="button" class="btn btn-light dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                Gestiones
                        </button>
                        <div class="dropdown-menu">
                            <a class="dropdown-item" href="/discador/opcion_proveedor">Gestion Telefonia</a>
                            
                            <a class="dropdown-item" href="/discador/agentes">Gestion de campo</a>
                            <a class="dropdown-item" href="#">Usuarios</a>
                            
                           
                        </div>
                        </div>
                        </li>

    <li class="nav-item active">
              
               
                            <div class="btn-group">
                            <button type="button" class="btn btn-light dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    Reportes
                            </button>
                            <div class="dropdown-menu">
                                <a class="dropdown-item" href="/discador/opcion_proveedor">Importador</a>
                                
                                <a class="dropdown-item" href="/discador/agentes">Monitoreo</a>
                           
                                
                               
                            </div>
                            </div>
                            </li>
    </ul>
    
</div>


</nav>


       
      );


    }

export default Header;