from django.conf.urls import url
from django.contrib import admin
from cdr.views import *


urlpatterns = [

    url(r'^list$', list),
    url(r'^ingresar$', ingresar),
    url(r'^salir$', salir),
    url(r'^$', ingresar),
    url(r'^audio/$', audio),    
    #url(r'^total$', list)
]
