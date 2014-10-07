#encoding:UTF-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,Group
from .models import *
from .forms import *
import datetime
# Create your views here.
def nuevo_usuario(request):
  	if request.method=="POST":
  		form=form_usuario(request.POST)
  		if(form.is_valid()):
  			new_user=request.POST["username"]
 			form.save()
 			usuario=User.objects.get(username=new_user)
 			usuario.is_active=False
 			usuario.save()
 			profile=perfil.objects.create(nick=usuario)
 			return HttpResponse("FELICIDADES")
 # 			return HttpResponseRedirect("/trivia/activar/")
 	else:
 		form=form_usuario()
	return render_to_response("usuarios/nuevo_usuario.html",{"form":form},RequestContext(request))
def logeo_usuario(request):
	if request.method=="POST":
		username=request.POST["username"]
		password=request.POST["password"]
		resultado=authenticate(username=username,password=password)
		if resultado is not None:
			if resultado.is_active:
				login(request,resultado)	
				return HttpResponseRedirect("/trivia/perfil/")	
			else:
				login(request, resultado)
				return HttpResponseRedirect("/trivia/activar/")
		else:
			return HttpResponseRedirect("/trivia/error/")
	return render_to_response("usuarios/logeo_usuario.html",{"form":AuthenticationForm()},RequestContext(request))
def vista_perfil(request):
 	return render_to_response("usuarios/perfil.html",RequestContext(request))
def logout_usuario(request):
 	logout(request)
 	return HttpResponseRedirect("/trivia/")
def activar_usuario(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/trivia/perfil/")
		else:
			if request.method=='POST':
				u=User.objects.get(username=usuario)
				profile=perfil.objects.get(nick=u)
				form=fperfil(request.POST,request.FILES,instance=profile)
				if form.is_valid():
					form.save()
					u.is_active=True
					u.save()
					return HttpResponseRedirect("/trivia/perfil/")
			else:
				form=fperfil()
			return render_to_response("usuarios/activar.html",{"form":form},RequestContext(request))
	else:
		return HttpResponseRedirect("/trivia/login/")
	# form=perfilForm()
	# return render_to_response("usuarios/activar.html",{"form":form},RequestContext(request))
def bienvenidofb(request):
	return HttpResponseRedirect("/trivia/")
def error(request):
	return render_to_response("usuarios/error.html",{},RequestContext(request))

