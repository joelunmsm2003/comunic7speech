# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-31 11:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colasIN', '0024_auto_20181231_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='agente',
            field=models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_agente', to='colasIN.Agente'),
        ),
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 31, 11, 52, 58, 217579)),
        ),
        migrations.AlterField(
            model_name='agente',
            name='t_estado',
            field=models.DateTimeField(db_column='t_estado', default=datetime.datetime(2018, 12, 31, 11, 52, 58, 217604)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 31, 11, 52, 58, 223308)),
        ),
        migrations.AlterField(
            model_name='logestadoagente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 31, 11, 52, 58, 216718)),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 31, 11, 52, 58, 223941), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 31, 11, 52, 58, 222818)),
        ),
    ]
