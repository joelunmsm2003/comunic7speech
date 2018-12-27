from django import forms
from django.forms import *
from colasIN.models import *
from django.forms import ModelForm,Textarea



class ReporteForm(ModelForm):
    class Meta:
        model = Produccion
        fields = ('numero_caso','tipo_caso','sub_tipo_caso','estado_incidencia')
        widgets = {
            'numero_caso':TextInput(attrs={'class':'form-control'}),
            'tipo_caso':TextInput(attrs={'class':'form-control'}),
            'estado_incidencia':TextInput(attrs={'class':'form-control'}),
            'sub_tipo_caso':TextInput(attrs={'class':'form-control'})
        }


class IncidenciaForm(ModelForm):
    class Meta:
        model = Produccion
        fields = ('numero_caso','estado_incidencia','sub_estado','detalle_lugar','fecha_atencion','unidad_reportante','dispositivo_origen','telefono_1','zona','accion_tomada','situacion')
        widgets = {
                'numero_caso':TextInput(attrs={'class':'form-control'}),
                'estado_incidencia':Select(attrs={'class':'form-control'}),
                'sub_estado':Select(attrs={'class':'form-control'}),
                'detalle_lugar':TextInput(attrs={'class':'form-control'}),
                'fecha_atencion':TextInput(attrs={'class':'form-control','type':'date'}),
                'unidad_reportante':TextInput(attrs={'class':'form-control'}),
                'dispositivo_origen':TextInput(attrs={'class':'form-control'}),
                'telefono_1':TextInput(attrs={'class':'form-control'}),
                'zona':TextInput(attrs={'class':'form-control'}),
                'accion_tomada':TextInput(attrs={'class':'form-control'}),
                'situacion':TextInput(attrs={'class':'form-control'})
                
            }
