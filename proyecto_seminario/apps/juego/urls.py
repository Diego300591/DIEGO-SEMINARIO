from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from proyecto_seminario.apps.juego.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_seminario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',pagina_principal),
    url(r'^usuarionuevo/$',registro_usuarios),
    url(r'^perfilusuario/$',crear_perfil),
    url(r'^logueousuario/$',Logueo_usuario),
    url(r'^vista/$',vista),
)