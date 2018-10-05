# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-04 23:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20180828_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBlaster',
            fields=[
                ('id_d_blaster', models.IntegerField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(blank=True, max_length=45)),
                ('uid', models.CharField(blank=True, db_column='UID', max_length=45)),
                ('fh_inicio', models.DateTimeField(blank=True, db_column='FH_inicio', null=True)),
                ('destino', models.CharField(blank=True, max_length=20)),
                ('audio', models.CharField(blank=True, max_length=200)),
                ('audio2', models.CharField(blank=True, max_length=200)),
                ('derivacion', models.CharField(blank=True, max_length=200)),
                ('lestado', models.IntegerField(blank=True, db_column='lEstado', null=True)),
                ('respuesta', models.IntegerField()),
                ('dtmf', models.IntegerField()),
                ('despedida', models.IntegerField()),
                ('oc7_1', models.IntegerField(blank=True, db_column='OC7_1', null=True)),
                ('oc7_2', models.IntegerField(db_column='OC7_2')),
                ('oc7_3', models.CharField(blank=True, db_column='OC7_3', max_length=10)),
                ('tduracion_ini', models.DateTimeField(blank=True, db_column='tDuracion_ini', null=True)),
                ('tduracion_fin', models.DateTimeField(blank=True, db_column='tDuracion_fin', null=True)),
                ('tduracion', models.IntegerField(db_column='tDuracion')),
                ('vclient', models.IntegerField(null=True)),
                ('cid', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'd_blaster',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DLlamadas',
            fields=[
                ('id_d_llamadas', models.IntegerField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(blank=True, max_length=45)),
                ('uid', models.CharField(blank=True, db_column='UID', max_length=45)),
                ('destino', models.CharField(blank=True, max_length=20)),
                ('audio', models.CharField(blank=True, max_length=200)),
                ('audio2', models.CharField(blank=True, max_length=200)),
                ('derivacion', models.CharField(blank=True, max_length=200)),
                ('dtmf', models.IntegerField()),
                ('despedida', models.IntegerField()),
                ('llam_flag', models.IntegerField(blank=True, null=True)),
                ('llam_uniqueid', models.CharField(blank=True, max_length=45)),
                ('llam_tipo', models.IntegerField(blank=True, null=True)),
                ('llam_canal', models.CharField(blank=True, max_length=100)),
                ('llam_estado', models.IntegerField(blank=True, null=True)),
                ('flagfin', models.IntegerField(blank=True, db_column='flagFIN', null=True)),
                ('t_ins', models.DateTimeField(db_column='T_INS')),
                ('t_pro', models.DateTimeField(db_column='T_PRO')),
                ('t_res', models.DateTimeField(db_column='T_RES')),
                ('t_fin1', models.DateTimeField(db_column='T_FIN1')),
                ('t_fin2', models.DateTimeField(db_column='T_FIN2')),
                ('d_timbrado', models.IntegerField()),
                ('d_ivr', models.IntegerField()),
                ('d_respuesta', models.IntegerField()),
                ('d_total', models.IntegerField()),
                ('respuesta01', models.IntegerField(db_column='Respuesta01')),
                ('respuesta02', models.IntegerField(db_column='Respuesta02')),
                ('codcorte', models.IntegerField(db_column='CodCorte')),
                ('vuelta', models.IntegerField()),
                ('vclient', models.IntegerField(null=True)),
                ('cid', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'd_llamadas',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 4, 23, 19, 22, 189067)),
        ),
        migrations.AlterField(
            model_name='api',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 4, 23, 19, 22, 188027)),
        ),
        migrations.AlterField(
            model_name='base',
            name='dni',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='base',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 4, 23, 19, 22, 186900)),
        ),
        migrations.AlterField(
            model_name='campania',
            name='fecha',
            field=models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2018, 10, 4, 23, 19, 22, 185360)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 4, 23, 19, 22, 184060)),
        ),
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 4, 23, 19, 22, 184653)),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 10, 4, 23, 19, 22, 183193)),
        ),
    ]
