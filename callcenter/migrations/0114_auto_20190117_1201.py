# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-17 12:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callcenter', '0113_auto_20190117_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 250551)),
        ),
        migrations.AlterField(
            model_name='api',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 247512)),
        ),
        migrations.AlterField(
            model_name='base',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 245092)),
        ),
        migrations.AlterField(
            model_name='campania',
            name='fecha',
            field=models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 241684)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 237002)),
        ),
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 240274)),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 235175)),
        ),
    ]
