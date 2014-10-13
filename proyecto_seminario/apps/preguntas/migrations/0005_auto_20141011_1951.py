# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0004_auto_20141011_1950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mpregunta',
            options={'permissions': ('mostrar_preguntas', 'permite ver las preguntas')},
        ),
    ]
