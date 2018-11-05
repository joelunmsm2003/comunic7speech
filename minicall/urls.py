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
from app.views import *
from django.conf.urls import include

admin.site.site_header = 'Comunica'


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^agente/(\d+)', m_agente),
	url(r'^ingresar/', ingresar),
	url(r'^monitor/', monitor),
	url(r'^monitor/', monitor),
	url(r'^api_agentes/', api_agentes),
    url(r'^actualiza_resultado/', actualiza_resultado),
    url(r'^lanzagestion/(\d+)/(\d+)', lanzagestion),
    url(r'^lanzafinllamada/(\d+)/(\d+)', lanzafinllamada),
    url(r'^lanzaestado/', lanzaestado),
    url(r'^api_agentes/', api_agentes),
    url(r'^discador/', include('discador.urls')),
]
