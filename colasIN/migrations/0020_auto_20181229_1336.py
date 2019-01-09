# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-29 13:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colasIN', '0019_merge_20181228_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='cierre',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 29, 13, 35, 59, 464459)),
        ),
        migrations.AlterField(
            model_name='agente',
            name='t_estado',
            field=models.DateTimeField(db_column='t_estado', default=datetime.datetime(2018, 12, 29, 13, 35, 59, 464482)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 29, 13, 35, 59, 470243)),
        ),
        migrations.AlterField(
            model_name='logestadoagente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 29, 13, 35, 59, 463745)),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 29, 13, 35, 59, 470748), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 29, 13, 35, 59, 469665)),
        ),
    ]
