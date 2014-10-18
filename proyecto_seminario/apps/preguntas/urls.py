from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from proyecto_seminario.apps.preguntas.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_seminario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^crearcategorias/$',crear_categoria),
    url(r'^crearpreguntas/$',crear_pregunta),
    url(r'^verpreguntas/$',ver_preguntas),
    url(r'^vercategorias/$',ver_categoria),
    url(r'^catrestringida/$',categoria_restringida),
    url(r'^pregrestringida/$',pregunta_restringida),
    url(r'^controlpreguntas/$',control_preguntas),
    url(r'^detallespreguntas/$',detalle_pregunta),
    url(r'^modificar/(?P<id>\d+)/$',modificar_pregunta,name='modificar_pregunta'),
    url(r'^verdetallepregunta/(?P<id>\d+)/$',ver_detalles,name='ver_detalles'),
    url(r'^eliminarpregunta/(?P<id>\d+)/$',eliminar_pregunta,name='eliminar_pregunta'),
    url(r'^preguntaseliminar/$',lista_preguntas_eliminar),
)