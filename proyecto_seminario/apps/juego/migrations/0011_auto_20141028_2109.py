# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0010_auto_20141005_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='nick',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
