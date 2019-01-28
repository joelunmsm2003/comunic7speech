# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-24 13:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colasIN', '0043_auto_20190121_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 24, 13, 19, 42, 383828)),
        ),
        migrations.AlterField(
            model_name='agente',
            name='t_estado',
            field=models.DateTimeField(db_column='t_estado', default=datetime.datetime(2019, 1, 24, 13, 19, 42, 383925)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 24, 13, 19, 42, 411985)),
        ),
        migrations.AlterField(
            model_name='logestadoagente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 24, 13, 19, 42, 380895)),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 13, 19, 42, 414010), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccionaudio',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 24, 13, 19, 42, 423463)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 13, 19, 42, 409644)),
        ),
    ]