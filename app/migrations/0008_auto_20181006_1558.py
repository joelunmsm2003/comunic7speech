# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-06 15:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181006_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 6, 15, 58, 37, 446268)),
        ),
        migrations.AlterField(
            model_name='api',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 6, 15, 58, 37, 445084)),
        ),
        migrations.AlterField(
            model_name='base',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 6, 15, 58, 37, 443993)),
        ),
        migrations.AlterField(
            model_name='campania',
            name='fecha',
            field=models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2018, 10, 6, 15, 58, 37, 442235)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 6, 15, 58, 37, 439693)),
        ),
        migrations.AlterField(
            model_name='dblaster',
            name='id_d_blaster',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 6, 15, 58, 37, 441579)),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 6, 15, 58, 37, 438436)),
        ),
    ]