from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
class perfil(models.Model):
 	nick=models.OneToOneField(User,unique=True,null=True,blank=True)
 	nombres=models.CharField(max_length=50)
 	apellidos=models.CharField(max_length=50)
 	avatar=models.ImageField(upload_to='media',null=True, blank=True, verbose_name='Imagen')
 	puntaje_total=models.PositiveIntegerField()
 	partidas_jugadas=models.PositiveIntegerField()



