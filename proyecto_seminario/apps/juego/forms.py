from django import forms
from django.forms import ModelForm
from .models import *
class UsuarioForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Usuario
		exclude=["fecha"]
class PerfilForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Perfil
class Logueo(forms.Form):
	nick=forms.CharField(max_length=200)
	password=forms.CharField(widget=forms.PasswordInput)
