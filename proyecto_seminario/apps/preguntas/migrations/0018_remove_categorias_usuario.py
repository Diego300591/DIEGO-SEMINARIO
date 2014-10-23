# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0017_categorias_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorias',
            name='usuario',
        ),
    ]
