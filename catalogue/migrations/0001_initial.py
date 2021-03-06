# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rol', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content_file', models.FileField(blank=True, upload_to='content')),
                ('score', models.FloatField(default=5)),
                ('type_of_content', models.IntegerField(choices=[(1, 'Pelicula'), (2, 'Serie')])),
                ('cover', models.ImageField(blank=True, upload_to='covers')),
                ('actors', models.ManyToManyField(blank=True, to='catalogue.Actor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField()),
                ('episode_file', models.FileField(upload_to='content')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Content')),
            ],
        ),
    ]
