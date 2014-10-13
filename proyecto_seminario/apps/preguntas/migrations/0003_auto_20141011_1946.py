# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0002_mpregunta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'permissions': ('vercategorias', 'permite ver las categorias')},
        ),
        migrations.AlterModelOptions(
            name='mpregunta',
            options={'permissions': ('verpreguntas', 'permite ver las preguntas')},
        ),
    ]
