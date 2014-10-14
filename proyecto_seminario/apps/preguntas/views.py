from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
import pdb
# Create your views here.
def crear_categoria(request):
	usuario=request.user #sirve para identificar el usuario
	if (not usuario.has_perm("preguntas.add_categorias")):
		return HttpResponseRedirect("/preguntas/catrestringida/")
	if request.method=="POST":
		fcategoria=categoriaForm(request.POST)
		if fcategoria.is_valid():
			fcategoria.save()
	fcategoria=categoriaForm()
	return render_to_response("preguntas/crear_categorias.html",{"fcategoria":fcategoria},RequestContext(request))
def crear_pregunta(request):
	usuario=request.user
	if(not usuario.has_perm("preguntas.add_mpregunta")):
		return HttpResponseRedirect("/preguntas/pregrestringida/")
	if request.method=="POST":
		fpregunta=preguntaForm(request.POST)
		if fpregunta.is_val+id():
			fpregunta.save()
	fpregunta=preguntaForm()
	return render_to_response("preguntas/crear_pregunta.html",{"fpregunta":fpregunta},RequestContext(request))
def ver_preguntas(request):
	lista=mpregunta.objects.all()
	return render_to_response("preguntas/verpreguntas.html",{"lista":lista},RequestContext(request))
def categoria_restringida(request):
	return render_to_response("preguntas/catrestringida.html",{},RequestContext(request))
def pregunta_restringida(request):
	return render_to_response("preguntas/pregrestringida.html",{},RequestContext(request))
def ver_categoria(request):
	lista=categorias.objects.all()
	return render_to_response("preguntas/vercategorias.html",{"lista":lista},RequestContext(request))