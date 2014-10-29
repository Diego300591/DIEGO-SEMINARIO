from django.db import models
# Create your models here.
class Usuario(models.Model):
	nick=models.CharField(max_length=200, unique=True)
	email=models.EmailField()
	password=models.CharField(max_length=200, null=True, blank=True)
	fecha=models.DateField(auto_now=True)
	def __unicode__(self):
		return self.nick