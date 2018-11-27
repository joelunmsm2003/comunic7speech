# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-16 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discador', '0006_remove_cartera_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarterasProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Cartera')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Proveedor')),
            ],
        ),
    ]