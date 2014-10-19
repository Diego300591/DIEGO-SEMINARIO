# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0010_auto_20141018_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='preguntas',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='tiempo_respuesta',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='tipo_partida',
        ),
    ]
