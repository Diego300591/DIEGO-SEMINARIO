from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto_seminario.apps.juego.views import *
from proyecto_seminario.apps.usuarios.views import *
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^trivia/',include("proyecto_seminario.apps.juego.urls")),
    url(r'^trivia/',include("proyecto_seminario.apps.usuarios.urls")),
    url(r'^trivia/',include("social_auth.urls")),
    #url(r'^trivia/',include("social.apps.django_app.urls",namespace='social')),
)
