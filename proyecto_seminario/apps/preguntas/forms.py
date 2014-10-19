from django import forms
from django.forms import ModelForm
from .models import *
class categoriaForm(forms.ModelForm):
	class Meta:
		model=categorias
class preguntaForm(ModelForm):
	class Meta:
		model=mpregunta
class partidaForm(ModelForm):
	class Meta:
		model=partida
		exclude=["usuario"]
