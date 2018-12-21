from django import forms
from django.forms import *
from colasIN.models import *





# class PacientesForm(ModelForm):
#     class Meta:
#         model = Pacientes
#         fields = '__all__'
#         exclude = ('user','foto') 
#         widgets = {
#             'dni':TextInput(attrs={'class':'form-control','type':'number'}),
# 			'domicilio':TextInput(attrs={'class':'form-control'}),
# 			'ciudad':Select(attrs={'class':'form-control'}),
# 			'telefono':TextInput(attrs={'class':'form-control','type':'number'}),
# 			'celular':TextInput(attrs={'class':'form-control','type':'number'}),
# 			'email':TextInput(attrs={'class':'form-control'}),
# 			'referenciado':TextInput(attrs={'class':'form-control'}),
#             'nombre':TextInput(attrs={'class':'form-control'}),
#             'apellido':TextInput(attrs={'class':'form-control'}),
#             'user':Select(attrs={'class':'form-control'}),
#             'nacimiento':TextInput(attrs={'type':'date','class':'form-control'})
#         }
#         error_messages = {
#             'Email': {
#                 'max_length': _("This writer's name is too long."),
#                 'required': _("Este campo es obligatorio"),
#             },
#             'Domicilio': {
#                 'max_length': _("This writer's name is too long."),
#                 'required': _("El domicilio es obligatorio"),
#             },

#         }
#         help_texts = {
#             'Email': _('Correo valido.'),
#             'Domicilio':_('Ingrese su direccion de casa'),
#         }

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