# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0006_auto_20141002_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name=b'Imagen', blank=True),
        ),
    ]
