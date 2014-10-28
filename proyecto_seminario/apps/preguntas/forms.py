from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.extras.widgets import *
tipos=(('public','Publico'),('private','Privado'))
cant_preguntas=(('0','10'),('1','20'),('2','30'),('3','40'),('4','50'))
tiempo=(('0','10 segundos'),('1','15 segundos'),('2','20 segundos'),('3','25 segundos'),('4','30 segundos'),('5','35 segundos'),('6','40 segundos'),('7','45 segundos'),('8','50 segundos'),('9','55 segundos'),('10','60 segundos'))
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
	tipo_partida=forms.ChoiceField(widget=forms.RadioSelect,choices=tipos)
	categorias_sel=forms.ModelMultipleChoiceField(queryset=categorias.objects.all(),widget=forms.CheckboxSelectMultiple())
	class Meta:
		model=partida
		exclude=["usuario"]
