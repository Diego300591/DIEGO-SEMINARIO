#encoding:UTF-8
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
class perfil(forms.ModelForm):
	class Meta:
		model=perfil
		exclude=['nick']

class form_usuario(UserCreationForm):
	username=forms.CharField(max_length=40, required=True, help_text=False, label='Nick')
	password2=forms.CharField(help_text=False, label="Contraseña de confirmación", widget=forms.PasswordInput())
	#first_name=forms.CharField(max_length=50)
	#last_name=forms.CharField(max_length=50)
	email=forms.EmailField(max_length=100, required=True, label='E-mail')
	class Meta:
		model=User
		fields=("username","password1","password2","email")
	def save(self,commit=True):
		user=super(form_usuario, self).save(commit=False)
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user

