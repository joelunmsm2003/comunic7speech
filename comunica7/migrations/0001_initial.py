# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-20 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('prefijo', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('empresa', models.CharField(blank=True, max_length=100, null=True)),
                ('distrito', models.CharField(blank=True, max_length=100, null=True)),
                ('ruc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios_Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comunica7.Usuarios')),
            ],
        ),
    ]
