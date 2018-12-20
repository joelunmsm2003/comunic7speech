# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-20 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('supervisor', models.CharField(blank=True, max_length=100, null=True)),
                ('anexo', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('t_inicio_gestion', models.CharField(blank=True, max_length=100, null=True)),
                ('t_fin_gestion', models.CharField(blank=True, max_length=100, null=True)),
                ('t_inicio_llamada', models.CharField(blank=True, max_length=100, null=True)),
                ('t_fin_llamada', models.CharField(blank=True, max_length=100, null=True)),
                ('t_inicio_espera', models.CharField(blank=True, max_length=100, null=True)),
                ('t_fin_espera', models.CharField(blank=True, max_length=100, null=True)),
                ('contactadas', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cartera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('dni', models.CharField(blank=True, max_length=100, null=True)),
                ('operacion', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('razon_social', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_persona', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_documento', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_documento', models.CharField(blank=True, max_length=100, null=True)),
                ('nombres', models.CharField(blank=True, max_length=100, null=True)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuadrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcliente', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_cuenta', models.CharField(blank=True, max_length=100, null=True)),
                ('moneda', models.CharField(blank=True, max_length=100, null=True)),
                ('producto', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_credito', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_clasificacion', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_vencimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_concecion', models.CharField(blank=True, max_length=1000, null=True)),
                ('nuemero_cuotas', models.CharField(blank=True, max_length=100, null=True)),
                ('dias_mora', models.CharField(blank=True, max_length=100, null=True)),
                ('tramo', models.CharField(blank=True, max_length=100, null=True)),
                ('rango_dias', models.CharField(blank=True, max_length=100, null=True)),
                ('segmento', models.CharField(blank=True, max_length=100, null=True)),
                ('grupo', models.CharField(blank=True, max_length=100, null=True)),
                ('ciclo', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_capital', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_interes', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_mora', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_otros', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_total', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_vencido', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_minimo', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_descuento', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_campania', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_cap_original', models.CharField(blank=True, max_length=100, null=True)),
                ('imp_prox_pago', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_prox_pago', models.CharField(blank=True, max_length=100, null=True)),
                ('observacion01', models.CharField(blank=True, max_length=100, null=True)),
                ('observacion02', models.CharField(blank=True, max_length=100, null=True)),
                ('observacion03', models.CharField(blank=True, max_length=100, null=True)),
                ('nro_tarjeta', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_deuda', models.CharField(blank=True, max_length=100, null=True)),
                ('id_gestor', models.CharField(blank=True, max_length=100, null=True)),
                ('cartera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_cartera', to='discador.Cartera')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubigeo', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('plano', models.CharField(blank=True, max_length=100, null=True)),
                ('cuadrante', models.CharField(blank=True, max_length=100, null=True)),
                ('fuente', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='discador.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Estado_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fuente_telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tipo de Gestiones',
            },
        ),
        migrations.CreateModel(
            name='IDGestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Industria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fuente', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('industria', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Industria')),
            ],
        ),
        migrations.CreateModel(
            name='ProveedorCarteras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Cartera')),
                ('negocio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Negocio')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_tipo_gestion', models.CharField(default=0, max_length=1)),
                ('peso_id_gestion', models.CharField(default=0, max_length=1)),
                ('peso_resultado', models.CharField(default=0, max_length=1)),
                ('peso_subresultado', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(default=0, max_length=1)),
                ('gestion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Gestion')),
                ('id_gestion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.IDGestion')),
                ('negocio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Negocio')),
                ('resultado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Resultado')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_tipo_gestion', models.CharField(default=0, max_length=1)),
                ('peso_id_gestion', models.CharField(default=0, max_length=1)),
                ('peso_resultado', models.CharField(default=0, max_length=1)),
                ('peso_subresultado', models.CharField(default=0, max_length=1)),
                ('estado', models.CharField(default=0, max_length=1)),
                ('gestion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Gestion')),
                ('id_gestion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.IDGestion')),
                ('negocio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Negocio')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Proveedor')),
                ('resultado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Resultado')),
            ],
        ),
        migrations.CreateModel(
            name='Segmentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('orden', models.CharField(blank=True, max_length=100, null=True)),
                ('cliente', models.CharField(blank=True, max_length=100, null=True)),
                ('base', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subresultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Justificaciones',
            },
        ),
        migrations.CreateModel(
            name='Telefonos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_documento', models.CharField(blank=True, max_length=100, null=True)),
                ('discado', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_contacto', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nombre', to='discador.Cliente')),
                ('fuente_telefono', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuente_telefono', to='discador.Fuente_telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_cartera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_dpto', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_prov', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_dist', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('dpto', models.CharField(blank=True, max_length=100, null=True)),
                ('provincia', models.CharField(blank=True, max_length=100, null=True)),
                ('distrito', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ubigeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='telefonos',
            name='tipo_telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_telefono', to='discador.Tipo_telefono'),
        ),
        migrations.AddField(
            model_name='scoreproveedor',
            name='subresultado',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Subresultado'),
        ),
        migrations.AddField(
            model_name='score',
            name='subresultado',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Subresultado'),
        ),
        migrations.AddField(
            model_name='mail',
            name='tipo_contacto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discador.Tipo_contacto'),
        ),
        migrations.AddField(
            model_name='direcciones',
            name='tipo_direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_direccion', to='discador.Tipo_direccion'),
        ),
        migrations.AddField(
            model_name='direcciones',
            name='tipo_domicilio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_domicilio', to='discador.Tipo_domicilio'),
        ),
    ]
