from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from proyecto_seminario.apps.usuarios.views import *
from proyecto_seminario.apps.preguntas.views import *
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^trivia/',include("proyecto_seminario.apps.usuarios.urls")),
    url(r'^preguntas/',include("proyecto_seminario.apps.preguntas.urls")),
    url(r'^trivia/',include("social_auth.urls")),
    url(r'^account/post_login/$',bienvenidofb),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^captcha/$',include('captcha.urls')),
)