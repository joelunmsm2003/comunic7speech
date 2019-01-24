#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import *
from colasIN.models import *
from django.forms import ModelForm,Textarea

# class AgendarForm(forms.Form):
# 	fecha = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control col-md-3','type':'date','required':'false'}))
# 	descripcion = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control','rows':"3",'required':'false'}))
    

class AgenteForm(ModelForm):
    class Meta:
        model = Agente
        fields = ('estado',)



class ProduccionForm(ModelForm):

    class Meta:
        model = Produccion
        fields = '__all__'
        exclude =('venta','usuario','direccion_rs','m_apellido_p','m_apellido_m','dni_c','boleta','factura','misma_direccion','mismo_cliente')
        widgets = {
            'nombre':TextInput(attrs={'class':'form-control'}),
            'fecha':TextInput(attrs={'class':'form-control'}),
            'telefono_1':TextInput(attrs={'class':'form-control'}),
            'telefono_2':TextInput(attrs={'class':'form-control'}),
            'cliente':TextInput(attrs={'class':'form-control'}),
            'apellido_p':TextInput(attrs={'class':'form-control'}),
            'apellido_m':TextInput(attrs={'class':'form-control'}),
            'dni':TextInput(attrs={'class':'form-control'}),
            'direccion':TextInput(attrs={'class':'form-control'}),
            'marca_vehiculo':TextInput(attrs={'class':'form-control'}),
            'modelo':TextInput(attrs={'class':'form-control'}),
            'version':TextInput(attrs={'class':'form-control'}),
            'anio':Select(attrs={'class':'form-control'}),
            'cilindrada':TextInput(attrs={'class':'form-control'}),
            'color':Select(attrs={'class':'form-control'}),
            'agente':Select(attrs={'class':'form-control'}),
            'kilometraje':TextInput(attrs={'class':'form-control'}),
            'placa':TextInput(attrs={'class':'form-control'}),
            'cantidad':TextInput(attrs={'class':'form-control'}),
            'marca_producto':TextInput(attrs={'class':'form-control'}),
            'modelo_bateria':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
            'cantidad_bu':TextInput(attrs={'class':'form-control'}),
            'descuento':TextInput(attrs={'class':'form-control'}),
            'precio_total':TextInput(attrs={'class':'form-control'}),
            'fecha_atencion':TextInput(attrs={'class':'form-control','type':'date'}),
            'hora_instalacion':TextInput(attrs={'class':'form-control','type':'time'}),
            'direccion_atencion':TextInput(attrs={'class':'form-control'}),
            'distrito':Select(attrs={'class':'form-control'}),
            'referencia':TextInput(attrs={'class':'form-control'}),
            'nombre_boleta':TextInput(attrs={'class':'form-control'}),
            'ruc':TextInput(attrs={'class':'form-control'}),
            'razon_social':TextInput(attrs={'class':'form-control'}),
            'pago':Select(attrs={'class':'form-control'}),
            'correo':TextInput(attrs={'class':'form-control'}),
            'atiende':Select(attrs={'class':'form-control'}),
            'almacen':Select(attrs={'class':'form-control'}),
            'gmail':TextInput(attrs={'class':'form-control'}),
            'status':Select(attrs={'class':'form-control'}),
            'observaciones':TextInput(attrs={'class':'form-control'}),
            'cierre':CheckboxInput(attrs={'class':'btn btn-default' }),
            
        }
        labels = {
            'anio':u'Año',
            'apellido_p':'Apellido Paterno',
            'apellido_m':'Apellido Materno',
            'cliente':'Nombres'
        }



class BusquedaForm(ModelForm):

    class Meta:
        model = Produccion
        fields =('telefono_1','cliente','apellido_p','apellido_m','razon_social')
        widgets = {

            'telefono_1':TextInput(attrs={'class':'form-control'}),
            'cliente':TextInput(attrs={'class':'form-control'}),
            'apellido_p':TextInput(attrs={'class':'form-control'}),
            'apellido_m':TextInput(attrs={'class':'form-control'}),
            'razon_social':TextInput(attrs={'class':'form-control'})
            
        }
        labels = {
            'telefono_1':u'Telefono',
            'apellido_p':'Apellido Paterno',
            'apellido_m':'Apellido Materno',
            'cliente':'Nombres'
        }



class VehiculosForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        exclude = ('version',) 
        widgets = {
            'nombre':TextInput(attrs={'class':'form-control'}),
            'modelo':TextInput(attrs={'class':'form-control'}),

            # 'dni':TextInput(attrs={'class':'form-control','type':'number'}),
            # 'domicilio':TextInput(attrs={'class':'form-control'}),
            # 'ciudad':Select(attrs={'class':'form-control'}),
            # 'telefono':TextInput(attrs={'class':'form-control','type':'number'}),
            # 'celular':TextInput(attrs={'class':'form-control','type':'number'}),
            # 'email':TextInput(attrs={'class':'form-control'}),
            # 'referenciado':TextInput(attrs={'class':'form-control'}),
            # 'nombre':TextInput(attrs={'class':'form-control'}),
            # 'apellido':TextInput(attrs={'class':'form-control'}),
            # 'user':Select(attrs={'class':'form-control'}),
            # 'nacimiento':TextInput(attrs={'type':'date','class':'form-control'})
        }

class BateriasForm(ModelForm):
    class Meta:
        model = Bateria
        fields = '__all__'
        exclude = ('codigo','equivalencia','cantidad','precio','cant_bat_usadas') 
        widgets = {
            'marca':TextInput(attrs={'class':'form-control'}),
            'modelo':TextInput(attrs={'class':'form-control'}),
            


            # 'dni':TextInput(attrs={'class':'form-control','type':'number'}),
            # 'domicilio':TextInput(attrs={'class':'form-control'}),
            # 'ciudad':Select(attrs={'class':'form-control'}),
            # 'telefono':TextInput(attrs={'class':'form-control','type':'number'}),
            # 'celular':TextInput(attrs={'class':'form-control','type':'number'}),
            # 'email':TextInput(attrs={'class':'form-control'}),
            # 'referenciado':TextInput(attrs={'class':'form-control'}),
            # 'nombre':TextInput(attrs={'class':'form-control'}),
            # 'apellido':TextInput(attrs={'class':'form-control'}),
            # 'user':Select(attrs={'class':'form-control'}),
            # 'nacimiento':TextInput(attrs={'type':'date','class':'form-control'})
        }