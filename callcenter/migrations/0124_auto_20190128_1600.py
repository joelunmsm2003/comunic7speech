# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-28 16:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callcenter', '0123_auto_20190124_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 2, 75013)),
        ),
        migrations.AlterField(
            model_name='api',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 2, 71279)),
        ),
        migrations.AlterField(
            model_name='base',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 2, 68227)),
        ),
        migrations.AlterField(
            model_name='campania',
            name='fecha',
            field=models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2019, 1, 28, 16, 0, 2, 64816)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 2, 60369)),
        ),
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 2, 63423)),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 2, 57934)),
        ),
    ]
