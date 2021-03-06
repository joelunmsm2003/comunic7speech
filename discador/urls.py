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


    url(r'^menu_proveedor/', proveedor),

    url(r'^menu_proveedor_1/', menu_proveedor_1),
    url(r'^menu_proveedor/', menu_proveedor),
    url(r'^api_proveedor/', api_proveedor),
    url(r'^api_estadocliente/', api_estadocliente),
    url(r'^api_tipocontacto/', api_tipo_contacto),
    url(r'^api_score/', api_score),
    url(r'^api_cartera/(\w+)/', api_cartera),
    url(r'^api_resultados/(\w+)/(\w+)/', api_resultados),
    url(r'^api_tipodomicilio/', api_tipodomicilio),

    




]
