from django import forms
from django.forms import ModelForm
from .models import *
tipos=(('public','Publico'),('private','Privado'))
categoria=categorias.objects.all()
class categoriaForm(forms.ModelForm):
	class Meta:
		model=categorias
		exclude=["usuario"]
class preguntaForm(ModelForm):
	class Meta:
		model=mpregunta
		exclude=["usuario"]
class partidaForm(ModelForm):
	tipo_partida=forms.CharField(widget=forms.RadioSelect(tipo=tipos))
	categorias_sel=forms.CharField(widget=forms.CheckboxSelectMultiple(categoria=categorias))
	class Meta:
		model=partida
		exclude=["usuario"]
