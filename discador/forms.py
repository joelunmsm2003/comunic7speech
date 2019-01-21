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



