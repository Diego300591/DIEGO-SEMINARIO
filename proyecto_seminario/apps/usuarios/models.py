from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
class perfil(models.Model):
 	nick=models.OneToOneField(User,unique=True)
 	nombres=models.CharField(max_length=50)
 	apellidos=models.CharField(max_length=50)
 	avatar=models.ImageField(upload_to='media',null=True,verbose_name='Imagen')
 	puntaje_total=models.PositiveIntegerField(default=0)
 	partidas_jugadas=models.PositiveIntegerField(default=0)
 	class Meta:
 		permissions=(("ver_perfil","permite ver el perfil"),("cambiar_perfil","permite modificar el perfil"),)
