from django import forms
from django.forms import *
from discador.models import *
from django.forms import ModelForm,Textarea





class ClientesForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombres','dni','telefono','numero_documento','fecha')
        widgets = {
            'nombres':TextInput(attrs={'class':'form-control'}),
            'dni':TextInput(attrs={'class':'form-control'}),
            'telefono':TextInput(attrs={'class':'form-control'}),
            'numero_documento':TextInput(attrs={'class':'form-control'}),
            'fecha':TextInput(attrs={'class':'form-control'})
        }

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ('__all__')
        widgets = {
            'nombre':TextInput(attrs={'class':'form-control'}),
            'dni':TextInput(attrs={'class':'form-control'}),
            'telefono':TextInput(attrs={'class':'form-control'}),
            'direccion':TextInput(attrs={'class':'form-control'}),
            'industria':TextInput(attrs={'class':'form-control'}),
            'email':TextInput(attrs={'class':'form-control'}),
            'contacto':TextInput(attrs={'class':'form-control'}),
            'obserbaciones':TextInput(attrs={'class':'form-control'}),
            'etado':TextInput(attrs={'class':'form-control'}),

        }


class AgenteForm(ModelForm):
    class Meta:
        model = Agente
        fields = ('nombre','direccion','telefono','grupo','user')
        widgets = {
            'nombre':TextInput(attrs={'class':'form-control'}),
            'direccion':TextInput(attrs={'class':'form-control'}),
            'telefono':TextInput(attrs={'class':'form-control'}),
            'grupo':TextInput(attrs={'class':'form-control'}),
            'user':Select(attrs={'class': 'form-control '}),
        }

class ProveedorCarteraForm(ModelForm):
    class Meta:
        model = ProveedorCarteras
        fields = ('__all__')
        widgets = {
            
            'proveedor': Select(attrs={'class': 'form-control '}),
            'cartera': Select(attrs={'class': 'form-control '}),
            'negocio': Select(attrs={'class': 'form-control '}),
           
        }






