# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0012_auto_20141018_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='preguntas',
            field=models.CharField(max_length=5, choices=[(b'0', b'10'), (b'1', b'20'), (b'2', b'30'), (b'3', b'40'), (b'4', b'50')]),
        ),
        migrations.AlterField(
            model_name='partida',
            name='tiempo_respuesta',
            field=models.CharField(max_length=5, choices=[(b'0', b'10'), (b'1', b'15'), (b'2', b'20'), (b'3', b'25'), (b'4', b'30'), (b'5', b'35'), (b'6', b'40'), (b'7', b'45'), (b'8', b'50'), (b'9', b'55'), (b'10', b'60')]),
        ),
    ]
