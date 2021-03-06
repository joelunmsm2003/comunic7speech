# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-05 20:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181105_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 5, 20, 6, 58, 320837)),
        ),
        migrations.AlterField(
            model_name='api',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 5, 20, 6, 58, 318416)),
        ),
        migrations.AlterField(
            model_name='base',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 5, 20, 6, 58, 315562)),
        ),
        migrations.AlterField(
            model_name='campania',
            name='fecha',
            field=models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2018, 11, 5, 20, 6, 58, 312473)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 5, 20, 6, 58, 309008)),
        ),
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 5, 20, 6, 58, 311369)),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 5, 20, 6, 58, 307483)),
        ),
    ]
