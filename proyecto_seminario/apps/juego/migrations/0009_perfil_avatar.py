# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name=b'Imagen', blank=True),
            preserve_default=True,
        ),
    ]
