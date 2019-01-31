# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-28 16:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colasIN', '0045_auto_20190124_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 1, 912851)),
        ),
        migrations.AlterField(
            model_name='agente',
            name='t_estado',
            field=models.DateTimeField(db_column='t_estado', default=datetime.datetime(2019, 1, 28, 16, 0, 1, 912953)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 1, 941423)),
        ),
        migrations.AlterField(
            model_name='logestadoagente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 1, 909617)),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 28, 16, 0, 1, 943437), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccionaudio',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 28, 16, 0, 1, 953078)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 28, 16, 0, 1, 939010)),
        ),
    ]