# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mpregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enunciado', models.TextField()),
                ('respuesta1', models.CharField(max_length=200)),
                ('respuesta2', models.CharField(max_length=200)),
                ('respuesta3', models.CharField(max_length=200)),
                ('respuesta4', models.CharField(max_length=200)),
                ('respuesta_correcta', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(to='preguntas.categorias')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
