from django import forms
from django.forms import ModelForm
from .models import *
class categoriaForm(ModelForm):
	class Meta:
		model=categorias
class preguntaForm(ModelForm):
	class Meta:
		model=mpregunta
