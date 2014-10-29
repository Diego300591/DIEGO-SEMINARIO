from django import forms
from django.forms import ModelForm
from .models import *
from captcha.fields import CaptchaField
class UsuarioForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Usuario
		exclude=["fecha"]
class Logueo(forms.Form):
	nick=forms.CharField(max_length=200)
	password=forms.CharField(widget=forms.PasswordInput)
#class CaptchaTestForm(forms.Form):
	#myfield = AnyOtherField()
	#captcha = CaptchaField()

