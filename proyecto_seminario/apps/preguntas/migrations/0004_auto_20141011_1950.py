# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0003_auto_20141011_1946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'permissions': ('ver_categoria', 'permite ver las categorias')},
        ),
        migrations.AlterModelOptions(
            name='mpregunta',
            options={'permissions': ('ver_preguntas', 'permite ver las preguntas')},
        ),
    ]
