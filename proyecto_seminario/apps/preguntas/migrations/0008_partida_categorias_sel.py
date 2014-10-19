# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0007_partida'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='categorias_sel',
            field=models.ManyToManyField(to='preguntas.categorias'),
            preserve_default=True,
        ),
    ]
