#encoding:UTF-8
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json
class fperfil(forms.ModelForm):
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
# class CaptchaTestForm(forms.Form):
#  	captcha=CaptchaField()
#  	class Meta:
#  		model=MyModel
# class AjaxExamlpeForm(CreateView):
# 	template_name=""
# 	form_class=AjaxForm
# 	def form_invalid(self,form):
# 		if self.request.is_ajax():
# 			to_json_response=dict()
# 			to_json_response['status']=0
# 			to_json_response['form_errors']=form_errors 
# 			to_json_response['new_cptch_key']=CaptchaStore.generate_key()
# 			to_json_response['new_cptch_image']=captcha_image_url(to_json_response['new_cptch_key'])
# 			return HttpResponse(json.dumps(to_json_response),content_type='application/json')
# 	def form_valid(self,form):
# 		form.save()
# 		if self.request.is_ajax():
# 			to_json_response=dict()
# 			to_json_response['status']=1
# 			to_json_response['new_cptch_key']=CaptchaStore.generate_key()
# 			to_json_response['new_cptch_image']=captcha_image_url(to_json_response['new_cptch_key'])
# 			return HttpResponse(json.dumps(to_json_response),content_type='application/json')