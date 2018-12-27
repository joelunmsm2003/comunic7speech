from django.conf.urls import url
from django.contrib import admin
from comunica7.views import *
from django.conf.urls import include



urlpatterns = [

	url(r'^ingresar/', ingresar),
	url(r'^dashboard/', dashboard)

]
