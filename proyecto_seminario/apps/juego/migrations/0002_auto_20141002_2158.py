# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(upload_to=b'media', verbose_name=b'Imagen', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='password',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nick',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
