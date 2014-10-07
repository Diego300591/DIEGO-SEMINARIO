# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20141006_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name=b'Imagen'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nick',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='partidas_jugadas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='puntaje_total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
