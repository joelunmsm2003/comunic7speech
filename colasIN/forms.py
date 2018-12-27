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
        exclude =('venta','usuario')
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
            'anio':TextInput(attrs={'class':'form-control'}),
            'cilindrada':TextInput(attrs={'class':'form-control'}),
            'color':TextInput(attrs={'class':'form-control'}),
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
            'hora_instalacion':TextInput(attrs={'class':'form-control','type':'date'}),
            'misma_direccion':TextInput(attrs={'class':'form-control'}),
            'direccion_atencion':TextInput(attrs={'class':'form-control'}),
            'distrito':TextInput(attrs={'class':'form-control'}),
            'referencia':TextInput(attrs={'class':'form-control'}),
            'boleta':TextInput(attrs={'class':'form-control'}),
            'mismo_cliente':TextInput(attrs={'class':'form-control'}),
            'nombre_boleta':TextInput(attrs={'class':'form-control'}),
            'm_apellido_p':TextInput(attrs={'class':'form-control'}),
            'm_apellido_m':TextInput(attrs={'class':'form-control'}),
            'dni_c':TextInput(attrs={'class':'form-control'}),
            'factura':TextInput(attrs={'class':'form-control'}),
            'ruc':TextInput(attrs={'class':'form-control'}),
            'razon_social':TextInput(attrs={'class':'form-control'}),
            'direccion_rs':TextInput(attrs={'class':'form-control'}),
            'pago':TextInput(attrs={'class':'form-control'}),
            'correo':TextInput(attrs={'class':'form-control'}),
            'atiende':TextInput(attrs={'class':'form-control'}),
            'almacen':TextInput(attrs={'class':'form-control'}),
            'gmail':TextInput(attrs={'class':'form-control'}),
            'status':TextInput(attrs={'class':'form-control'}),
            'observaciones':TextInput(attrs={'class':'form-control'})
        }



class NuevoCAsoForm(ModelForm):
    class Meta:
        model = Produccion
        fields = ('tipo_caso', 'sub_tipo_caso','detalle')
       
        widgets = {
            'tipo_caso':TextInput(attrs={'class':'form-control'}),
            'sub_tipo_caso':TextInput(attrs={'class':'form-control'}),
            'detalle':Textarea(attrs={'class':'form-control'}),

            
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