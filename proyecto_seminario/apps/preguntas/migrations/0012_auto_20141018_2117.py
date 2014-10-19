# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0011_auto_20141018_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='preguntas',
            field=models.CharField(default=10, max_length=5, choices=[(0, b'10'), (1, b'20'), (2, b'30'), (3, b'40'), (4, b'50')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partida',
            name='tiempo_respuesta',
            field=models.CharField(default=20, max_length=5, choices=[(0, b'10'), (1, b'15'), (2, b'20'), (3, b'25'), (4, b'30'), (5, b'35'), (6, b'40'), (7, b'45'), (8, b'50'), (9, b'55'), (10, b'60')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partida',
            name='tipo_partida',
            field=models.CharField(default=30, max_length=200, choices=[(b'public', b'Publico'), (b'private', b'Privado')]),
            preserve_default=False,
        ),
    ]
