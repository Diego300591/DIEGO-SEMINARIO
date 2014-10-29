# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0020_auto_20141028_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='tiempo_respuesta',
            field=models.CharField(max_length=5, choices=[(b'10', b'10'), (b'15', b'15'), (b'20', b'20'), (b'25', b'25'), (b'30', b'30'), (b'35', b'35'), (b'40', b'40'), (b'45', b'45'), (b'50', b'50'), (b'55', b'55'), (b'60', b'60')]),
        ),
    ]
