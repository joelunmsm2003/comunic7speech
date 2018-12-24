from django.conf.urls import url
from django.contrib import admin
from colasIN.views import *
from django.conf.urls import  include, url



urlpatterns = [
    

    url(r'^usuarios/$', usuarios, name='usuarios'),
    url(r'^vehiculos/$', vehiculos),
    url(r'^reporte/$', reporte),
    url(r'^importar/$', importar),
    url(r'^login/$', login2),
    url(r'^subir/$', subir),
    url(r'^masacre/$', masacre),
    url(r'^distrito/$', dstlima),
    url(r'^anio/$', anio),
    url(r'^colores/$', color),
    url(r'^ingresar/$',ingresar),
    url(r'^dashboard/$', dashboard),
    url(r'^album/$', album),
    url(r'^paciente/$', paciente),
    url(r'^nuevopaciente/$', nuevopaciente),
    url(r'^guardar$', guardar),
    url(r'^api_motorisado/', api_motorisado),
    url(r'^api_motorisado/', api_motorisado),
    url(r'^monitor_agente/(\d+)/(\d+)/', m_agente),
    url(r'^lanzallamada/(\d+)/(\d+)', lanzallamada),
    url(r'^lanzafinllamada/(\d+)/(\d+)', lanzafinllamada),



]