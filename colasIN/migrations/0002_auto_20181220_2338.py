# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-20 23:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('colasIN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anio_v',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Atiende',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
                ('celular', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=1000, null=True)),
                ('equivalencia', models.CharField(blank=True, max_length=1000, null=True)),
                ('cantidad', models.CharField(blank=True, max_length=1000, null=True)),
                ('marca', models.CharField(blank=True, max_length=1000, null=True)),
                ('modelo', models.CharField(blank=True, max_length=1000, null=True)),
                ('precio', models.CharField(blank=True, max_length=1000, null=True)),
                ('descuento', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colores_v',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_social', models.CharField(blank=True, max_length=1000, null=True)),
                ('ruc', models.CharField(blank=True, max_length=1000, null=True)),
                ('direc_r_social', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2018, 12, 20, 23, 38, 4, 384387), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)')),
                ('telefono_1', models.CharField(blank=True, help_text='N\xfamero de tel\xe9fono desde donde llama el cliente', max_length=1000, null=True)),
                ('telefono_2', models.CharField(blank=True, help_text='Otro nmero de tel\xe9fono de contacto', max_length=1000, null=True)),
                ('cliente', models.CharField(blank=True, help_text='Nombre del Cliente', max_length=1000, null=True)),
                ('apellido_p', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Apellido Paterno')),
                ('apellido_m', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Apellido Materno')),
                ('dni', models.CharField(blank=True, help_text='Otro nmero de dni', max_length=1000, null=True)),
                ('direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('marca_vehiculo', models.CharField(blank=True, max_length=1000, null=True)),
                ('modelo', models.CharField(blank=True, max_length=1000, null=True)),
                ('version', models.CharField(blank=True, max_length=1000, null=True)),
                ('cilindrada', models.CharField(blank=True, max_length=1000, null=True)),
                ('kilometraje', models.CharField(blank=True, max_length=1000, null=True)),
                ('placa', models.CharField(blank=True, max_length=1000, null=True)),
                ('cantidad', models.CharField(blank=True, max_length=1000, null=True)),
                ('marca_producto', models.CharField(blank=True, max_length=1000, null=True)),
                ('modelo_bateria', models.CharField(blank=True, max_length=1000, null=True)),
                ('precio', models.CharField(blank=True, max_length=1000, null=True)),
                ('cantidad_bu', models.CharField(blank=True, help_text='Cantidad de baterias usadas', max_length=1000, null=True)),
                ('descuento', models.CharField(blank=True, max_length=1000, null=True)),
                ('precio_total', models.CharField(blank=True, max_length=1000, null=True)),
                ('fecha_atencion', models.DateField(blank=True, max_length=1000, null=True)),
                ('hora_instalacion', models.TimeField(blank=True, max_length=1000, null=True)),
                ('misma_direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion_atencion', models.CharField(blank=True, max_length=1000, null=True)),
                ('referencia', models.CharField(blank=True, max_length=1000, null=True)),
                ('boleta', models.BooleanField(default=True, max_length=1000)),
                ('mismo_cliente', models.CharField(blank=True, max_length=1000, null=True)),
                ('nombre_boleta', models.CharField(blank=True, max_length=1000, null=True)),
                ('m_apellido_p', models.CharField(blank=True, max_length=1000, null=True)),
                ('m_apellido_m', models.CharField(blank=True, max_length=1000, null=True)),
                ('dni_c', models.CharField(blank=True, max_length=1000, null=True)),
                ('factura', models.BooleanField(default=True, max_length=1000)),
                ('ruc', models.CharField(blank=True, max_length=1000, null=True)),
                ('razon_social', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion_rs', models.CharField(blank=True, max_length=1000, null=True)),
                ('correo', models.CharField(blank=True, max_length=1000, null=True)),
                ('gmail', models.CharField(blank=True, max_length=1000, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=1000, null=True)),
                ('almacen', models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_almacen', to='colasIN.Almacen')),
                ('anio', models.ForeignKey(blank=True, help_text='Anio', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_nombre', to='colasIN.Anio_v')),
                ('atiende', models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_atiende', to='colasIN.Atiende')),
                ('color', models.ForeignKey(blank=True, help_text='Color', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_nombre', to='colasIN.Colores_v')),
                ('distrito', models.ForeignKey(blank=True, help_text='Distrito', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_nombre', to='colasIN.Distrito')),
                ('pago', models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, to='colasIN.Pago')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
                ('modelo', models.CharField(blank=True, max_length=1000, null=True)),
                ('version', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Supervisor',
        ),
        migrations.AddField(
            model_name='produccion',
            name='status',
            field=models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_status', to='colasIN.Status'),
        ),
        migrations.AddField(
            model_name='produccion',
            name='usuario',
            field=models.ForeignKey(blank=True, help_text='Usuarios', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_modelo', to=settings.AUTH_USER_MODEL),
        ),
    ]