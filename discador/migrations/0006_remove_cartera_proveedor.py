# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-16 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discador', '0005_carteraproveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartera',
            name='proveedor',
        ),
    ]