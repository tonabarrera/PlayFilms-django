# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 22:27
from __future__ import unicode_literals

import catalogue.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20170613_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_file',
            field=models.FileField(blank=True, max_length=250, upload_to=catalogue.models.get_upload_path_movie, verbose_name='archivo de video'),
        ),
        migrations.AlterField(
            model_name='content',
            name='cover',
            field=models.ImageField(max_length=250, upload_to=catalogue.models.get_upload_path_cover, verbose_name='Portada'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='episode_file',
            field=models.FileField(max_length=250, upload_to=catalogue.models.get_upload_path_serie, verbose_name='Archivo del episodio'),
        ),
    ]