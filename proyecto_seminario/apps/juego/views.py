#encoding:UTF-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
import datetime
# Create your views here.
def pagina_principal(request):
	fecha=datetime.datetime.now()
	return render_to_response("principal.html",{"fecha":fecha},RequestContext(request))
def registro_usuarios(request):
	usuario=UsuarioForm()
	errorMsn=""
	if request.method=="POST":
		usuario=UsuarioForm(request.POST)
		p=usuario.save(commit=False)
		p.fecha=datetime.datetime.now().date()
		if usuario.is_valid():
			usuario.save()
			return HttpResponseRedirect("/trivia/")
		else:
			errorMsn="DATOS INCORRECTOS!!!"
	return render_to_response("trivia/usuarionuevo.html",{"error":errorMsn,"form_usuario":usuario},RequestContext(request))
def crear_perfil(request):
	if request.method=="POST":
		perfil=PerfilForm(request.POST)
		if perfil.is_valid():
			perfil.save()
			return HttpResponseRedirect("/trivia/")
	perfil=PerfilForm()
	return render_to_response("trivia/crear_perfil.html",{"form_perfil":perfil},RequestContext(request))


