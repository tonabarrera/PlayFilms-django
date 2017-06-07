# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 01:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0010_auto_20170605_2248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditcard',
            options={'verbose_name': 'tarjeta de credito', 'verbose_name_plural': 'Tarjetas de credito'},
        ),
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'Historial', 'verbose_name_plural': 'Historial'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Perfil de usuario', 'verbose_name_plural': 'Perfiles de usuario'},
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userprofiles.UserProfile', verbose_name='perfil de usuario'),
        ),
        migrations.AlterField(
            model_name='history',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Content', verbose_name='contenido'),
        ),
        migrations.AlterField(
            model_name='history',
            name='is_favorite',
            field=models.BooleanField(default=False, verbose_name='es favorito'),
        ),
        migrations.AlterField(
            model_name='history',
            name='score',
            field=models.PositiveIntegerField(blank=True, default=5, verbose_name='puntuación'),
        ),
        migrations.AlterField(
            model_name='history',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofiles.UserProfile', verbose_name='perfil de usuario'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default_app_avatar.png', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type_of_user',
            field=models.IntegerField(choices=[(1, 'Premium'), (2, 'Estandar')], default=2, verbose_name='tipo de usuario'),
        ),
    ]
