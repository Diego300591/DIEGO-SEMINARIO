#encoding:UTF-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,Group,Permission
from django.contrib.sessions.models import Session
from .models import *
from .forms import *
from django.forms import forms
from recaptcha.client import captcha
# from captcha.fields import CaptchaField
import datetime
import pdb
# Create your views here.
def pagina_principal(request):
	menu=permisos(request)
	fecha=datetime.datetime.now()
	return render_to_response("principal.html",{"fecha":fecha,"menu":menu},RequestContext(request))
def nuevo_usuario(request):
	menu=permisos(request)
  	if request.method=="POST":
  		form=form_usuario(request.POST)
  		if(form.is_valid()):
  			new_user=request.POST["username"]
 			form.save()
 			usuario=User.objects.get(username=new_user)
 			usuario.is_active=False
 			usuario.save()
 			profile=perfil.objects.create(nick=usuario)
 			return HttpResponseRedirect("/trivia/")
 # 			return HttpResponseRedirect("/trivia/activar/")
 	else:
 		form=form_usuario()
	return render_to_response("usuarios/nuevo_usuario.html",{"form":form, "menu":menu},RequestContext(request))
def logeo_usuario(request):
	menu=permisos(request)
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if form.is_valid:
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado is not None:
				if resultado.is_active:
					login(request,resultado)	
					del request.session['cont']
					return HttpResponseRedirect("/trivia/perfil/")	
				else:
					login(request, resultado)
					return HttpResponseRedirect("/trivia/activar/")
			else:
				request.session['cont']=request.session['cont']+1
				aux=request.session['cont']
				if aux>3:
					return HttpResponseRedirect("/trivia/captchas")
				estado=True
				mensaje="Error en los datos "+str(aux)
				datos={'form':form,'estado':estado,'mensaje':mensaje}
				return render_to_response("usuarios/logeo_usuario.html",datos,RequestContext(request))
			#return HttpResponseRedirect("/trivia/error/")
	else:
		request.session['cont']=0
		form=AuthenticationForm()
	return render_to_response("usuarios/logeo_usuario.html",{"form":form, "menu":menu},RequestContext(request))
def vista_perfil(request):
	menu=permisos(request)
 	return render_to_response("usuarios/perfil.html",{"menu":menu},RequestContext(request))
def logout_usuario(request):
	menu=permisos(request)
 	logout(request)
 	return HttpResponseRedirect("/trivia/")
def activar_usuario(request):
	menu=permisos(request)
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
	menu=permisos(request)
	return HttpResponseRedirect("/trivia/")
	return render_to_response("bienvenidofb.html",{"menu":menu},RequestContext(request))
def error(request):
	return render_to_response("usuarios/error.html",{},RequestContext(request))
# def peticion(request):
#   	if request.method=="POST":
#   		form=CaptchaTestForm(request.POST)
#   		if form.is_valid():
#   			ser_humano=True
#   	form=CaptchaTestForm()
#   	return render_to_response("usuarios/captcha.html",locals(),{"form":form},RequestContext(request))
def permisos(request):
	listadepermisos=[]
	usuario=request.user
	if usuario.has_perm("preguntas.add_categorias"):
		listadepermisos.append({"url":"/preguntas/crearcategorias/","label":"agregar categorias"})
	if usuario.has_perm("preguntas.add_mpregunta"):
		listadepermisos.append({"url":"/preguntas/crearpreguntas/","label":"agregar preguntas"})
	if usuario.has_perm("preguntas.mostrar_preguntas"):
		listadepermisos.append({"url":"/preguntas/verpreguntas/","label":"ver preguntas"})
	if usuario.has_perm("preguntas.ver_categoria"):
		listadepermisos.append({"url":"/preguntas/vercategorias/","label":"ver categorias"})
	return listadepermisos

def myview(request):
	if request.method == "POST":
		edit_form = EditForm(request.POST)
		response = captcha.submit(
			request.POST.get('recaptcha_challenge_field'),
			request.POST.get('recaptcha_response_field'),
			'6LdRDfwSAAAAAA5J38RyDQyHw2oWxwQgkXORu759 ',
			request.META['REMOTE_ADDR'],)
		if response.is_valid:
			#captcha_response = "ERES HUMANO: %(data)s" % {'data':edit_form.data['nombre']}
			return HttpResponseRedirect("/trivia/")
		else:
			captcha_response = 'DEBES SER UN ROBOT'
		return render_to_response("usuarios/captcha2.html",{'edit_form':edit_form, 'captcha_response':captcha_response},RequestContext(request))
	else:
		edit_form=EditForm()
		return render_to_response("usuarios/captcha2.html",{"edit_form":edit_form},RequestContext(request))


