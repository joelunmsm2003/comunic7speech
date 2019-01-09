# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-08 17:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colasIN', '0029_auto_20190108_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccionaudio',
            name='agente',
            field=models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_agente_produccion_audio', to='colasIN.Agente'),
        ),
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 8, 17, 47, 7, 106913)),
        ),
        migrations.AlterField(
            model_name='agente',
            name='t_estado',
            field=models.DateTimeField(db_column='t_estado', default=datetime.datetime(2019, 1, 8, 17, 47, 7, 106935)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 8, 17, 47, 7, 112681)),
        ),
        migrations.AlterField(
            model_name='logestadoagente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 8, 17, 47, 7, 106192)),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 8, 17, 47, 7, 113229), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccionaudio',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 8, 17, 47, 7, 115607)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 8, 17, 47, 7, 112115)),
        ),
    ]
