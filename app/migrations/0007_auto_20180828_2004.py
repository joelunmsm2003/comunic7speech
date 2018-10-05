# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-28 20:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180828_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='base',
            old_name='cliente',
            new_name='apellido',
        ),
        migrations.AddField(
            model_name='base',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='base',
            name='id_cliente',
            field=models.CharField(blank=True, max_length=100, verbose_name='ID Cliente'),
        ),
        migrations.AlterField(
            model_name='campania',
            name='fecha',
            field=models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2018, 8, 28, 20, 4, 15, 487713)),
        ),
    ]
