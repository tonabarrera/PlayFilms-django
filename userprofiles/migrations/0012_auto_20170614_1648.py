# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import userprofiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0011_auto_20170606_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='owner',
            field=models.CharField(blank=True, max_length=45, verbose_name='Dueño'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default_app_avatar.png', upload_to=userprofiles.models.get_upload_path),
        ),
    ]
