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