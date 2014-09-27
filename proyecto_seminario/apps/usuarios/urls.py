from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto_seminario.apps.usuarios.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_seminario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^nuevousuario/$',nuevo_usuario),
    url(r'^login/$',logeo_usuario),
    url(r'^perfil/$',perfil),
    url(r'^logout/$',logout_usuario),
)