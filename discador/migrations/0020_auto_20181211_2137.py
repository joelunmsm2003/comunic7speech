# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-11 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discador', '0019_auto_20181207_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='proveedor',
            name='industria',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Industria'),
        ),
    ]
