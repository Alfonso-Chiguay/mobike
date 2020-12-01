from django import forms
from .models import UsuarioMobike

class FormularioLogin(forms.Form):
    usuario = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Password", widget=forms.PasswordInput, strip=False)



class FormularioCrearUsuario(forms.ModelForm):

     class Meta:
         model = UsuarioMobike
         fields = '__all__'
