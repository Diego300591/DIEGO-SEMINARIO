from django import forms
from django.forms import ModelForm
from .models import *
class perfilForm(ModelForm):
	class Meta:
		model=perfil
		exclude=['nick']