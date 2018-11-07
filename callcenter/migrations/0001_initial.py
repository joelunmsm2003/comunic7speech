# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-07 19:22
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anexo', models.IntegerField(blank=True, null=True)),
                ('fono', models.IntegerField(blank=True, null=True)),
                ('destino', models.IntegerField(blank=True, null=True)),
                ('duracion', models.TimeField(blank=True, null=True)),
                ('atendidas', models.IntegerField(blank=True, null=True)),
                ('contactadas', models.IntegerField(blank=True, null=True)),
                ('est_ag_predictivo', models.IntegerField(blank=True, null=True)),
                ('canal', models.CharField(blank=True, max_length=100)),
                ('fecha', models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 22, 16, 269391))),
            ],
            options={
                'verbose_name': 'Agente',
            },
        ),
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('metodo', models.CharField(blank=True, max_length=100, null=True)),
                ('header', models.CharField(blank=True, max_length=100, null=True)),
                ('body', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 22, 16, 268050))),
            ],
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=100, null=True)),
                ('nombres', models.CharField(blank=True, max_length=100, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True)),
                ('dni', models.CharField(blank=True, max_length=100, null=True, verbose_name='DNI')),
                ('telefono_1', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono_2', models.CharField(blank=True, max_length=100, null=True)),
                ('importe', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_promesa', models.CharField(blank=True, max_length=100, null=True)),
                ('deuda', models.CharField(blank=True, max_length=100, null=True)),
                ('deuda_pendiente', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 22, 16, 266545))),
            ],
        ),
        migrations.CreateModel(
            name='Campania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2018, 11, 7, 19, 22, 16, 264034))),
                ('archivo', models.FileField(upload_to='static')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('fecha', models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 22, 16, 262249))),
            ],
        ),
        migrations.CreateModel(
            name='DBlaster',
            fields=[
                ('id_d_blaster', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(blank=True, db_column='UID', max_length=45)),
                ('fh_inicio', models.DateTimeField(blank=True, db_column='FH_inicio', null=True)),
                ('destino', models.CharField(blank=True, max_length=20)),
                ('parametro_1', models.CharField(blank=True, max_length=20, verbose_name='Deuda')),
                ('parametro_2', models.CharField(blank=True, max_length=20, verbose_name='Nombres')),
                ('parametro_3', models.CharField(blank=True, max_length=20, verbose_name='Fecha Promesa')),
                ('audio', models.CharField(blank=True, max_length=200)),
                ('audio2', models.CharField(blank=True, max_length=200)),
                ('derivacion', models.CharField(blank=True, max_length=200)),
                ('lestado', models.IntegerField(blank=True, db_column='lEstado', null=True)),
                ('respuesta', models.IntegerField(blank=True, null=True)),
                ('dtmf', models.IntegerField(blank=True, null=True)),
                ('despedida', models.IntegerField(blank=True, null=True)),
                ('tipo', models.IntegerField(blank=True, null=True)),
                ('oc7_1', models.IntegerField(blank=True, db_column='OC7_1', null=True)),
                ('oc7_2', models.IntegerField(blank=True, db_column='OC7_2', null=True)),
                ('oc7_3', models.CharField(blank=True, db_column='OC7_3', max_length=10)),
                ('tduracion_ini', models.DateTimeField(blank=True, db_column='tDuracion_ini', null=True)),
                ('tduracion_fin', models.DateTimeField(blank=True, db_column='tDuracion_fin', null=True)),
                ('tduracion', models.IntegerField(blank=True, db_column='tDuracion', null=True)),
                ('vclient', models.IntegerField(null=True)),
                ('cid', models.CharField(blank=True, max_length=45)),
                ('campania', models.ForeignKey(blank=True, db_column='evento', null=True, on_delete=django.db.models.deletion.CASCADE, to='callcenter.Campania')),
                ('cliente', models.ForeignKey(blank=True, db_column='cliente', null=True, on_delete=django.db.models.deletion.CASCADE, to='callcenter.Cliente')),
            ],
            options={
                'db_table': 'callcenter_d_blaster',
                'managed': True,
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
                ('resultado', models.CharField(blank=True, max_length=200)),
                ('id_d_blaster', models.ForeignKey(blank=True, db_column='id_d_blaster', null=True, on_delete=django.db.models.deletion.CASCADE, to='callcenter.DBlaster')),
            ],
            options={
                'db_table': 'callcenter_d_llamadas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('fecha', models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 22, 16, 263435))),
            ],
        ),
        migrations.CreateModel(
            name='Estadocampania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('fecha', models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 22, 16, 261362))),
                ('user', models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='callcenteruser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='campania',
            name='cliente',
            field=models.ForeignKey(blank=True, db_column='cliente', null=True, on_delete=django.db.models.deletion.CASCADE, to='callcenter.Cliente'),
        ),
        migrations.AddField(
            model_name='campania',
            name='estado',
            field=models.ForeignKey(blank=True, db_column='estado', null=True, on_delete=django.db.models.deletion.CASCADE, to='callcenter.Estadocampania'),
        ),
        migrations.AddField(
            model_name='base',
            name='campania',
            field=models.ForeignKey(blank=True, db_column='campania', null=True, on_delete=django.db.models.deletion.CASCADE, to='callcenter.Campania'),
        ),
        migrations.AddField(
            model_name='agente',
            name='estado',
            field=models.ForeignKey(blank=True, db_column='estado', null=True, on_delete=django.db.models.deletion.CASCADE, to='callcenter.Estado'),
        ),
        migrations.AddField(
            model_name='agente',
            name='supervisor',
            field=models.ForeignKey(blank=True, db_column='supervisor', null=True, on_delete=django.db.models.deletion.CASCADE, to='callcenter.Supervisor'),
        ),
        migrations.AddField(
            model_name='agente',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='callcenteruseragente', to=settings.AUTH_USER_MODEL),
        ),
    ]
