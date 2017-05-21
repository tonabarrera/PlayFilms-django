# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='score',
            field=models.PositiveIntegerField(blank=True, default=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='default_app_avatar.pgn', upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type_of_user',
            field=models.IntegerField(choices=[(1, 'Premium'), (2, 'Estandar')], default=2),
        ),
    ]
