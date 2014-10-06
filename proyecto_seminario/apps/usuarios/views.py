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
 		form=UserCreationForm(request.POST)
 		if(form.is_valid()):
 			form.save()
 			return HttpResponseRedirect("/trivia/activar/")
	return render_to_response("usuarios/nuevo_usuario.html",{"form":UserCreationForm()},RequestContext(request))
def logeo_usuario(request):
	if request.method=="POST":
		username=request.POST["username"]
		password=request.POST["password"]
		resultado=authenticate(username=username,password=password)
		if(resultado):
			login(request,resultado)	
			return HttpResponseRedirect("/trivia/")	
		else:
			return HttpResponseRedirect("/trivia/error/")
	return render_to_response("usuarios/logeo_usuario.html",{"form":AuthenticationForm()},RequestContext(request))
def perfil(request):
 	return render_to_response("usuarios/perfil.html",RequestContext(request))
def logout_usuario(request):
 	logout(request)
 	return HttpResponseRedirect("/trivia/")
def activar_usuario(request):
	if request.method=='POST':
		form=perfilForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/trivia/")
	form=perfilForm()
	return render_to_response("usuarios/activar.html",{"form":form},RequestContext(request))
def bienvenidofb(request):
	return HttpResponseRedirect("/trivia/")
def error(request):
	return render_to_response("usuarios/error.html",{},RequestContext(request))

