# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 01:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20170521_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name_plural': 'actores'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['title', 'score'], 'verbose_name': 'contenido', 'verbose_name_plural': 'contenido'},
        ),
        migrations.AlterModelOptions(
            name='episode',
            options={'verbose_name': 'Episodio', 'verbose_name_plural': 'Episodios'},
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='content',
            name='actors',
            field=models.ManyToManyField(blank=True, to='catalogue.Actor', verbose_name='actores'),
        ),
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Category', verbose_name='Categorias'),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_file',
            field=models.FileField(blank=True, upload_to='content', verbose_name='archivo de video'),
        ),
        migrations.AlterField(
            model_name='content',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers', verbose_name='Portada'),
        ),
        migrations.AlterField(
            model_name='content',
            name='score',
            field=models.FloatField(default=5, verbose_name='puntuación'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='content',
            name='type_of_content',
            field=models.IntegerField(choices=[(1, 'Pelicula'), (2, 'Serie')], verbose_name='Tipo de contenido'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='episode_file',
            field=models.FileField(upload_to='content', verbose_name='Archivo del episodio'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]