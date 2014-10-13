from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from proyecto_seminario.apps.usuarios.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_seminario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',pagina_principal),
    url(r'^nuevousuario/$',nuevo_usuario),
    url(r'^login/$',logeo_usuario),
    url(r'^perfil/$',vista_perfil),
    url(r'^logout/$',logout_usuario),
    url(r'^activar/$',activar_usuario),
    url(r'^error/$',error),
    #url(r'^captchas/$',peticion),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)