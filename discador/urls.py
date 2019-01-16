"""minicall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from discador.views import *


urlpatterns = [


    url(r'^proveedor_score/', proveedor_score),

    url(r'^menu_proveedor_1/', menu_proveedor_1),

    url(r'^api_proveedor/', api_proveedores),
    url(r'^api_estadocliente/', api_estadocliente),
    url(r'^api_tipocontacto/', api_tipo_contacto),
    url(r'^api_score/', api_score),
    url(r'^api_cartera/(\w+)', api_cartera),
    url(r'^api_carteras/', api_carteras),
    url(r'^api_carteras_proveedor/(\d+)', api_carteras_proveedor),
    url(r'^api_carteras_negocios/(\d+)/(\d+)', api_carteras_negocios),
    url(r'^api_id_gestion/(\d+)', api_id_gestion),
    url(r'^api_resultados/', api_resultados),
    url(r'^api_proveedor_detalle/(\d+)', api_proveedor),
    url(r'^api_detalle_cartera/(\d+)', api_detalle_cartera),
    url(r'^api_detalle_proveedor_cartera_negocio/(\d+)/(\d+)/(\d+)', api_detalle_proveedor_cartera_negocio),
    url(r'^api_resultados_gestion/(\d+)', api_resultados_gestion),
    url(r'^api_subresultados/(\d+)', api_subresultados),
    url(r'^api_tipodomicilio/', api_tipodomicilio),
    url(r'^api_producto/', api_producto),
    url(r'^api_cuadrante/', api_cuadrante),
    url(r'^api_plano/', api_plano),
    url(r'^api_gestiones/', api_gestion),
    url(r'^api_cuentas/', api_cuentas),
    url(r'^api_busca_score/', api_busca_score),
    url(r'^api_negocios/', api_negocios),
    url(r'^api_proveedor_cartera_negocio/', api_proveedor_cartera_negocio),
    url(r'^usuarios/', usuarios),
    url(r'^marcador/', marcador),
    url(r'^importador/',importador),
    url(r'^opcion_proveedor/',opcion_proveedor),
    url(r'^opcion_asigna_score/(\d+)/(\d+)/(\d+)',opcion_asigna_score),
    url(r'^agentes/',agentes),
    url(r'^opcion_score/',opcion_score),
    url(r'^opcion_clientes/',opcion_clientes),
 
    url(r'^carteras/(\d+)',carteras),
    url(r'^guardaproveedor/',guardaproveedor),
    url(r'^api_detalle_cuentas/(\d+)', api_detalle_cuentas),
    url(r'^api_telefonos', api_telefonos),
    url(r'^api_asigna_score', api_asigna_score),
    url(r'^api_obtiene_estado_score/(\d+)/(\d+)/(\d+)', api_obtiene_estado_score),
    url(r'^api_negocios/', api_negocios),
    url(r'^api_resultados_negocio/(\d+)', api_resultados_negocio),
    url(r'^subescores/', subescores),
    url(r'^subecuentas/', subecuentas),
    url(r'^subetelefonos/', subetelefonos),
    url(r'^subeclientes/', subeclientes),
    url(r'^traeagentes/',traeagentes),
    url(r'^api_agentes/',api_agentes),
    url(r'^borrar/', borrar),
    


    



    ############

    url(r'^opcion_asigna_score/(\d+)/(\d+)/(\d+)',opcion_asigna_score),



]
