# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-19 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discador', '0003_auto_20181219_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreproveedor',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Proveedor'),
        ),
    ]
