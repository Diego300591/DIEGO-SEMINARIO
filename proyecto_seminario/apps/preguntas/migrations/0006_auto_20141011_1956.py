# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0005_auto_20141011_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'permissions': (('ver_categoria', 'permite ver las categorias'),)},
        ),
        migrations.AlterModelOptions(
            name='mpregunta',
            options={'permissions': (('mostrar_preguntas', 'permite ver las preguntas'), ('ver_categoria_pregunta', 'permite ver las categorias de una pregunta'))},
        ),
    ]
