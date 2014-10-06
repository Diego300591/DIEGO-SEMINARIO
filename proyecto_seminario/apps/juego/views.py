 #encoding:UTF-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from .models import *
from .forms import *
import datetime
import json
# Create your views here.
def pagina_principal(request):
	fecha=datetime.datetime.now()
	return render_to_response("principal.html",{"fecha":fecha},RequestContext(request))
def registro_usuarios(request):
	errorMsn=""
	usuario=UsuarioForm()
	if request.method=="POST":
		usuario=UsuarioForm(request.POST)
		request.session["nick"]=request.POST["nick"]
		request.session["password"]=request.POST["password"]
		p=usuario.save(commit=False)
		p.fecha=datetime.datetime.now().date()
		if usuario.is_valid():
			usuario.save()
			return HttpResponseRedirect("/trivia/perfilusuario")
		else:
			errorMsn="DATOS INCORRECTOS!!!"
	return render_to_response("trivia/usuarionuevo.html",{"error":errorMsn,"form_usuario":usuario},RequestContext(request))
def crear_perfil(request):
	if request.method=="POST":
		#nick=request.session["nick"]
		#nombres=request.POST["nombres"]
		#apellidos=request.POST["apellidos"]
		#clave=request.session["password"]
		#avatar=request.session["avatar"]
		#puntaje=request.POST["puntaje_total"]
		#partidas=request.POST["partidas"]
		#aux=PerfilForm({nick=nick,password=clave})
		#perfil=PerfilForm(instance=aux)
#<<<<<<< HEAD
		perfil=PerfilForm(request.POST,request.FILES,)
#=======
		#perfil=PerfilForm(request.POST)
#>>>>>>> 0ba6c164108dc57261780eee9b573dcc26bbea9e
		if perfil.is_valid():
			perfil.save()
			return HttpResponseRedirect("/trivia/")
	perfil=PerfilForm()
	return render_to_response("trivia/crear_perfil.html",{"form_perfil":perfil},RequestContext(request))
def Logueo_usuario(request):
	errorMsn=""
	if request.method=="POST":
		log=Logueo(request.POST)
		if log.is_valid():
			data=log.cleaned_data
			s=Usuario.objects.filter(nick=data["nick"],password=data["password"])
			if(len(s)>0):
				return HttpResponseRedirect("/trivia/")
			else:
				errorMsn="NOMBRE DE USUARIO INCORRECTO!!!"
		else:
			errorMsn="DATOS INVALIDOS!!!"
	logueo=Logueo() 
	return render_to_response("trivia/logueo.html",{"error":errorMsn,"logueo":logueo},RequestContext(request))
def vista(request):
	dato=Perfil.objects.all()
	return render_to_response("trivia/vista.html",{"dato":dato},RequestContext(request))
# def captcha(request):
# 	if request.POST:
# 		form = CaptchaTestForm(request.POST)
# 		if form.is_valid():
# 			human=True
# 		else:
# 			form=CaptchaTestForm()
# 	return render_to_response("trivia/captcha.html",locals(),{},RequestContext(request))
# #class CaptchaFormulario(CreateView):
# 	#template_name=''
# 	#form_class=CaptchaTestForm()
# def form_invalid(self, form):
# 	if self.request.is_ajax():
# 		to_json_response = dict()
# 		to_json_response['status']=0
# 		to_json_response['form_errors']=form.errors 
# 		to_json_response['new_cptch_key']=CaptchaStore.generate_key()
# 		to_json_response['new_cptch_image']=captcha_image_url(to_json_response['new_cptch_key'])
# 		return HttpResponse(json.dumps(to_json_response),content_type='application/json')
# def form_valid(self, form):
# 	form.save()
# 	if self.request.is_ajax():
# 		to_json_response = dict()
# 		to_json_response['status']=1
# 		to_json_response['new_cptch_key']=CaptchaStore.generate_key()
# 		to_json_response['new_cptch_image']=captcha_image_url(to_json_response['new_cptch_key'])
# 		return HttpResponse(json.dumps(to_json_response),content_type='application/json')
