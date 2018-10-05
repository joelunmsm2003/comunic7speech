# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-28 19:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cargada', models.DateTimeField(blank=True, db_column=b'fecha cargada', null=True)),
                ('estado', models.TextField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('tipo', models.IntegerField(blank=True, null=True)),
                ('discado', models.IntegerField(blank=True, null=True)),
                ('factor', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('prefijo', models.IntegerField(blank=True, null=True)),
                ('troncal', models.IntegerField(blank=True, null=True)),
                ('timbrado1', models.IntegerField(blank=True, null=True)),
                ('timbrado2', models.IntegerField(blank=True, null=True)),
                ('grabacion', models.IntegerField(blank=True, null=True)),
                ('t1', models.IntegerField(blank=True, null=True)),
                ('t2', models.IntegerField(blank=True, null=True)),
                ('t3', models.IntegerField(blank=True, null=True)),
                ('o_error_cnt', models.IntegerField(blank=True, null=True)),
                ('o_nocontesto_cnt', models.IntegerField(blank=True, null=True)),
                ('canales', models.IntegerField(blank=True, null=True)),
                ('timbrados', models.IntegerField(blank=True, null=True)),
                ('htinicio', models.TimeField(blank=True, null=True)),
                ('htfin', models.TimeField(blank=True, null=True)),
                ('mxllamada', models.IntegerField(blank=True, null=True)),
                ('llamadaxhora', models.IntegerField(blank=True, null=True)),
                ('hombreobjetivo', models.IntegerField(blank=True, null=True)),
                ('archivo', models.FileField(upload_to=b'files')),
                ('tgestion', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('inactividad', models.IntegerField(blank=True, null=True)),
                ('acd', models.IntegerField(blank=True, db_column=b'ACD', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, db_column=b'user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='campania',
            name='supervisor',
            field=models.ForeignKey(blank=True, db_column=b'supervisor', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Supervisor'),
        ),
        migrations.AddField(
            model_name='campania',
            name='usuario',
            field=models.ForeignKey(blank=True, db_column=b'usuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
