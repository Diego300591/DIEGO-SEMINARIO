from django.db import models
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
	categoria=models.ForeignKey(categorias)
	enunciado=models.TextField()
	respuesta1=models.CharField(max_length=200)
	respuesta2=models.CharField(max_length=200)
	respuesta3=models.CharField(max_length=200)
	respuesta4=models.CharField(max_length=200)
	respuesta_correcta=models.CharField(max_length=200)
	class Meta():
		permissions=(
			("mostrar_preguntas","permite ver las preguntas"),
			("ver_categoria_pregunta","permite ver las categorias de una pregunta"),
		)


