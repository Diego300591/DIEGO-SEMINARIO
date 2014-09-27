# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to=b'photos')),
                ('puntaje_total', models.PositiveIntegerField()),
                ('partidas', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=200)),
                ('fecha', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='perfil',
            name='nick',
            field=models.ForeignKey(to='juego.Usuario', unique=True),
            preserve_default=True,
        ),
    ]
