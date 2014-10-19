# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0006_auto_20141011_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='partida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('jugadores', models.PositiveIntegerField()),
                ('tipo_partida', models.CharField(max_length=200, choices=[(b'public', b'Publico'), (b'private', b'Privado')])),
                ('preguntas', models.CharField(max_length=5, choices=[(0, b'10'), (1, b'20'), (2, b'30'), (3, b'40'), (4, b'50')])),
                ('tiempo_respuesta', models.CharField(max_length=5, choices=[(0, b'10'), (1, b'15'), (2, b'20'), (3, b'25'), (4, b'30'), (5, b'35'), (6, b'40'), (7, b'45'), (8, b'50'), (9, b'55'), (10, b'60')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
