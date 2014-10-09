from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.
def crear_categoria(request):
	if request.method=="POST":
		fcategoria=categoriaForm(request.POST)
		if fcategoria.is_valid():
			fcategoria.save()
	fcategoria=categoriaForm()
	return render_to_response("preguntas/crear_categorias.html",{"fcategoria":fcategoria},RequestContext(request))
def crear_pregunta(request):
	if request.method=="POST":
		fpregunta=preguntaForm(request.POST)
		if fpregunta.is_valid():
			fpregunta.save()
	fpregunta=preguntaForm()
	return render_to_response("preguntas/crear_pregunta.html",{"fpregunta":fpregunta},RequestContext(request))