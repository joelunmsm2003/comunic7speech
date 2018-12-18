# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-18 04:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discador', '0025_auto_20181218_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.ProveedorCarteras')),
                ('score', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Resultado')),
            ],
        ),
    ]
