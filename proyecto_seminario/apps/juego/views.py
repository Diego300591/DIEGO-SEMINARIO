 #encoding:UTF-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from .forms import *
import datetime
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
		perfil=PerfilForm(request.POST,request.FILES,)
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
def bienvenidofb(request):
	return render_to_response("bienvenidofb.html",{},RequestContext(request))
def vista(request):
	dato=Perfil.objects.all()
	return render_to_response("trivia/vista.html",{"dato":dato},RequestContext(request))
