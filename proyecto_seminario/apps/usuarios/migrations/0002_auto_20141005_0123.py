# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nick',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
