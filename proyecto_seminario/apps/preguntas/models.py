from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection
# Create your models here.
class categorias(models.Model):
	nombre=models.CharField(max_length=50)
	def __unicode__(self):
		return self.nombre
	class Meta():
		permissions=(
			("ver_categoria","permite ver las categorias"),
		)
class mpregunta(models.Model):
	usuario=models.ForeignKey(User, null=True)
	categoria=models.ForeignKey(categorias)
	enunciado=models.TextField()
	respuesta1=models.CharField(max_length=200)
	respuesta2=models.CharField(max_length=200)
	respuesta3=models.CharField(max_length=200)
	respuesta4=models.CharField(max_length=200)
	respuesta_correcta=models.CharField(max_length=200)
	def __unicode__(self):
		return self.enunciado
	class Meta():
		permissions=(
			("mostrar_preguntas","permite ver las preguntas"),
			("ver_categoria_pregunta","permite ver las categorias de una pregunta"),
		)
class partida(models.Model):
	tipos=(('public','Publico'),('private','Privado'))
	cant_preguntas=(('0','10'),('1','20'),('2','30'),('3','40'),('4','50'))
	tiempo=(('0','10'),('1','15'),('2','20'),('3','25'),('4','30'),('5','35'),('6','40'),('7','45'),('8','50'),('9','55'),('10','60'))
	titulo=models.CharField(max_length=200)
	jugadores=models.PositiveIntegerField()
	tipo_partida=models.CharField(max_length=200,choices=tipos)
	preguntas=models.CharField(max_length=5, choices=cant_preguntas)
	tiempo_respuesta=models.CharField(max_length=5,choices=tiempo)
	categorias_sel=models.ManyToManyField(categorias, blank=False)
	usuario=models.ForeignKey(User)
	def __unicode__(self):
		return self.titulo



