from django.conf.urls import url
from django.contrib import admin
from speech.views import *
from django.conf.urls import include



urlpatterns = [

	url(r'^agente/(\d+)', m_agente),
	
	url(r'^monitor/', monitor),
	url(r'^api_agentes/', api_agentes),
    url(r'^actualiza_resultado/', actualiza_resultado),
    url(r'^lanzagestion/(\d+)/(\d+)', lanzagestion),
    url(r'^lanzafinllamada/(\d+)/(\d+)', lanzafinllamada),
    url(r'^lanzaestado/', lanzaestado),
    url(r'^api_agentes/', api_agentes),
]
