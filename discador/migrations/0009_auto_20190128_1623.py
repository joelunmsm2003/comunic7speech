# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-28 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discador', '0008_auto_20190128_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestiones_externas',
            name='anio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gestiones_externas',
            name='mes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]