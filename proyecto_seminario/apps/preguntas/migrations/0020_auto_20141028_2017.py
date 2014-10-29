# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0019_auto_20141024_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='preguntas',
            field=models.CharField(max_length=5, choices=[(b'10', b'10'), (b'20', b'20'), (b'30', b'30'), (b'40', b'40'), (b'50', b'50')]),
        ),
        migrations.AlterField(
            model_name='partida',
            name='tiempo_respuesta',
            field=models.CharField(max_length=5, choices=[(b'10 segundos', b'10 segundos'), (b'15 segundos', b'15 segundos'), (b'20 segundos', b'20 segundos'), (b'25 segundos', b'25 segundos'), (b'30 segundos', b'30 segundos'), (b'35 segundos', b'35 segundos'), (b'40 segundos', b'40 segundos'), (b'45 segundos', b'45 segundos'), (b'50 segundos', b'50 segundos'), (b'55 segundos', b'55 segundos'), (b'60 segundos', b'60 segundos')]),
        ),
    ]
