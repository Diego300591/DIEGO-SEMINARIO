# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0018_remove_categorias_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='tiempo_respuesta',
            field=models.CharField(max_length=5, choices=[(b'0', b'10 segundos'), (b'1', b'15 segundos'), (b'2', b'20 segundos'), (b'3', b'25 segundos'), (b'4', b'30 segundos'), (b'5', b'35 segundos'), (b'6', b'40 segundos'), (b'7', b'45 segundos'), (b'8', b'50 segundos'), (b'9', b'55 segundos'), (b'10', b'60 segundos')]),
        ),
    ]
