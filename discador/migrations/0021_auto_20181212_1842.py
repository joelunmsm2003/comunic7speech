# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-12 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discador', '0020_auto_20181211_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDGestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='id_gestion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.IDGestion'),
        ),
    ]
