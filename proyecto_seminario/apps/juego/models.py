from django.db import models
# Create your models here.
class Usuario(models.Model):
	nick=models.CharField(max_length=200, unique=True)
	email=models.EmailField()
	password=models.CharField(max_length=200)
	fecha=models.DateField(auto_now=True)
	def __unicode__(self):
		return self.nick
class Perfil(models.Model):
	nick=models.ForeignKey(Usuario, unique=True)
	nombres=models.CharField(max_length=50)
	apellidos=models.CharField(max_length=50)
	password=models.CharField(max_length=200, unique=True)
	avatar=models.ImageField(upload_to='media', blank=True, verbose_name='Imagen')
	puntaje_total=models.PositiveIntegerField()
	partidas=models.PositiveIntegerField()
	def __unicode__(self):
		return self.nombres+" "+self.apellidos