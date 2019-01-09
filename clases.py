# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CallcenterAgente(models.Model):
    anexo = models.IntegerField(blank=True, null=True)
    fono = models.IntegerField(blank=True, null=True)
    destino = models.IntegerField(blank=True, null=True)
    duracion = models.TimeField(blank=True, null=True)
    atendidas = models.IntegerField(blank=True, null=True)
    contactadas = models.IntegerField(blank=True, null=True)
    est_ag_predictivo = models.IntegerField(blank=True, null=True)
    canal = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    estado = models.ForeignKey('CallcenterEstado', models.DO_NOTHING, db_column='estado', blank=True, null=True)
    supervisor = models.ForeignKey('CallcenterSupervisor', models.DO_NOTHING, db_column='supervisor', blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callcenter_agente'


class CallcenterApi(models.Model):
    host = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    metodo = models.CharField(max_length=100, blank=True, null=True)
    header = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'callcenter_api'


class CallcenterBase(models.Model):
    codigo = models.CharField(max_length=100, blank=True, null=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(max_length=100, blank=True, null=True)
    telefono_1 = models.CharField(max_length=100, blank=True, null=True)
    telefono_2 = models.CharField(max_length=100, blank=True, null=True)
    importe = models.CharField(max_length=100, blank=True, null=True)
    fecha_promesa = models.CharField(max_length=100, blank=True, null=True)
    deuda = models.CharField(max_length=100, blank=True, null=True)
    deuda_pendiente = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField()
    campania = models.ForeignKey('CallcenterCampania', models.DO_NOTHING, db_column='campania', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callcenter_base'


class CallcenterCampania(models.Model):
    fecha_cargada = models.DateTimeField(db_column='fecha cargada')  # Field renamed to remove unsuitable characters.
    archivo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    cliente = models.ForeignKey('CallcenterCliente', models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    estado = models.ForeignKey('CallcenterEstadocampania', models.DO_NOTHING, db_column='estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callcenter_campania'


class CallcenterCliente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'callcenter_cliente'


class CallcenterDBlaster(models.Model):
    id_d_blaster = models.AutoField(primary_key=True)
    uid = models.CharField(db_column='UID', max_length=45)  # Field name made lowercase.
    fh_inicio = models.DateTimeField(db_column='FH_inicio', blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(max_length=20)
    parametro_1 = models.CharField(max_length=20)
    parametro_2 = models.CharField(max_length=20)
    parametro_3 = models.CharField(max_length=20)
    audio = models.CharField(max_length=200)
    audio2 = models.CharField(max_length=200)
    derivacion = models.CharField(max_length=200)
    lestado = models.IntegerField(db_column='lEstado', blank=True, null=True)  # Field name made lowercase.
    respuesta = models.IntegerField(blank=True, null=True)
    dtmf = models.IntegerField(blank=True, null=True)
    despedida = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    oc7_1 = models.IntegerField(db_column='OC7_1', blank=True, null=True)  # Field name made lowercase.
    oc7_2 = models.IntegerField(db_column='OC7_2', blank=True, null=True)  # Field name made lowercase.
    oc7_3 = models.CharField(db_column='OC7_3', max_length=10)  # Field name made lowercase.
    tduracion_ini = models.DateTimeField(db_column='tDuracion_ini', blank=True, null=True)  # Field name made lowercase.
    tduracion_fin = models.DateTimeField(db_column='tDuracion_fin', blank=True, null=True)  # Field name made lowercase.
    tduracion = models.IntegerField(db_column='tDuracion', blank=True, null=True)  # Field name made lowercase.
    vclient = models.IntegerField(blank=True, null=True)
    cid = models.CharField(max_length=45)
    evento = models.ForeignKey(CallcenterCampania, models.DO_NOTHING, db_column='evento', blank=True, null=True)
    cliente = models.ForeignKey(CallcenterCliente, models.DO_NOTHING, db_column='cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callcenter_d_blaster'


class CallcenterDLlamadas(models.Model):
    id_d_llamadas = models.IntegerField(primary_key=True)
    cliente = models.CharField(max_length=45)
    uid = models.CharField(db_column='UID', max_length=45)  # Field name made lowercase.
    destino = models.CharField(max_length=20)
    audio = models.CharField(max_length=200)
    audio2 = models.CharField(max_length=200)
    derivacion = models.CharField(max_length=200)
    dtmf = models.IntegerField()
    despedida = models.IntegerField()
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45)
    llam_tipo = models.IntegerField(blank=True, null=True)
    llam_canal = models.CharField(max_length=100)
    llam_estado = models.IntegerField(blank=True, null=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True)  # Field name made lowercase.
    t_ins = models.DateTimeField(db_column='T_INS')  # Field name made lowercase.
    t_pro = models.DateTimeField(db_column='T_PRO')  # Field name made lowercase.
    t_res = models.DateTimeField(db_column='T_RES')  # Field name made lowercase.
    t_fin1 = models.DateTimeField(db_column='T_FIN1')  # Field name made lowercase.
    t_fin2 = models.DateTimeField(db_column='T_FIN2')  # Field name made lowercase.
    d_timbrado = models.IntegerField()
    d_ivr = models.IntegerField()
    d_respuesta = models.IntegerField()
    d_total = models.IntegerField()
    respuesta01 = models.IntegerField(db_column='Respuesta01')  # Field name made lowercase.
    respuesta02 = models.IntegerField(db_column='Respuesta02')  # Field name made lowercase.
    codcorte = models.IntegerField(db_column='CodCorte')  # Field name made lowercase.
    vuelta = models.IntegerField()
    vclient = models.IntegerField(blank=True, null=True)
    cid = models.CharField(max_length=45)
    resultado = models.CharField(max_length=200)
    id_d_blaster = models.ForeignKey(CallcenterDBlaster, models.DO_NOTHING, db_column='id_d_blaster', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callcenter_d_llamadas'


class CallcenterEstado(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'callcenter_estado'


class CallcenterEstadocampania(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'callcenter_estadocampania'


class CallcenterSupervisor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callcenter_supervisor'


class Cdr(models.Model):
    acctid = models.BigIntegerField(primary_key=True)
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cdr'


class ColasinAcd(models.Model):
    id_acd = models.AutoField()
    did_campana = models.CharField(db_column='DID_Campana', max_length=45)  # Field name made lowercase.
    numero_llamado = models.CharField(db_column='Numero_Llamado', max_length=45)  # Field name made lowercase.
    numero_entrante = models.CharField(db_column='Numero_Entrante', max_length=45)  # Field name made lowercase.
    channel_entrante = models.CharField(db_column='Channel_Entrante', max_length=50)  # Field name made lowercase.
    tiempo = models.IntegerField(db_column='Tiempo')  # Field name made lowercase.
    flag = models.IntegerField()
    uniqueid = models.CharField(max_length=30)
    fin = models.IntegerField()
    age_nombre = models.CharField(max_length=100, blank=True, null=True)
    tie_ing = models.DateTimeField()
    tie_acd = models.DateTimeField()
    tie_tra = models.DateTimeField()
    tie_con = models.DateTimeField()
    tie_fin = models.DateTimeField()
    tie_acw = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    sql = models.IntegerField()
    codhu = models.IntegerField(db_column='CodHU')  # Field name made lowercase.
    bill = models.IntegerField()
    asterisk = models.IntegerField()
    audio = models.CharField(unique=True, max_length=100)
    valorllamada = models.CharField(max_length=200)
    id_ori_usuario = models.IntegerField()
    llam_estado = models.IntegerField()
    anexo = models.IntegerField()
    duration = models.IntegerField()
    espera = models.IntegerField()
    pais = models.CharField(max_length=10)
    g_id1 = models.CharField(max_length=100)
    g_id2 = models.CharField(max_length=100)
    g_id3 = models.CharField(max_length=100)
    g_id4 = models.CharField(max_length=100)
    g_id5 = models.CharField(max_length=100)
    g_id6 = models.CharField(max_length=100)
    g_id7 = models.CharField(max_length=100)
    g_id8 = models.CharField(max_length=100)
    g_id9 = models.CharField(max_length=100)
    g_id10 = models.CharField(max_length=100)
    accountcode = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'colasIN_acd'


class ColasinAgente(models.Model):
    anexo = models.IntegerField(blank=True, null=True)
    fono = models.IntegerField(blank=True, null=True)
    destino = models.IntegerField(blank=True, null=True)
    duracion = models.TimeField(blank=True, null=True)
    atendidas = models.IntegerField(blank=True, null=True)
    contactadas = models.IntegerField(blank=True, null=True)
    est_ag_predictivo = models.IntegerField(blank=True, null=True)
    canal = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    estado = models.ForeignKey('ColasinEstadoagente', models.DO_NOTHING, db_column='estado', blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)
    nombre = models.CharField(max_length=1000, blank=True, null=True)
    t_estado = models.DateTimeField()
    id_estado = models.IntegerField(blank=True, null=True)
    acd = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'colasIN_agente'


class ColasinAlbum(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_album'


class ColasinAlmacen(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_almacen'


class ColasinAnioV(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_anio_v'


class ColasinArticle(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'colasIN_article'


class ColasinAtiende(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)
    celular = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_atiende'


class ColasinBateria(models.Model):
    codigo = models.CharField(max_length=1000, blank=True, null=True)
    equivalencia = models.CharField(max_length=1000, blank=True, null=True)
    cantidad = models.CharField(max_length=1000, blank=True, null=True)
    marca = models.CharField(max_length=1000, blank=True, null=True)
    modelo = models.CharField(max_length=1000, blank=True, null=True)
    precio = models.CharField(max_length=1000, blank=True, null=True)
    descuento = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_bateria'


class ColasinClientes(models.Model):
    codigo = models.CharField(max_length=100, blank=True, null=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(max_length=100, blank=True, null=True)
    telefono_1 = models.CharField(max_length=100, blank=True, null=True)
    telefono_2 = models.CharField(max_length=100, blank=True, null=True)
    importe = models.CharField(max_length=100, blank=True, null=True)
    fecha_promesa = models.CharField(max_length=100, blank=True, null=True)
    deuda = models.CharField(max_length=100, blank=True, null=True)
    deuda_pendiente = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'colasIN_clientes'


class ColasinColoresV(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_colores_v'


class ColasinDistrito(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_distrito'


class ColasinEstadoagente(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_estadoagente'


class ColasinFactura(models.Model):
    r_social = models.CharField(max_length=1000, blank=True, null=True)
    ruc = models.CharField(max_length=1000, blank=True, null=True)
    direc_r_social = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_factura'


class ColasinLogestadoagente(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)
    fecha = models.DateTimeField()
    estado = models.ForeignKey(ColasinEstadoagente, models.DO_NOTHING, db_column='estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_logestadoagente'


class ColasinPago(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_pago'


class ColasinProduccion(models.Model):
    fecha = models.DateTimeField()
    telefono_1 = models.CharField(max_length=1000, blank=True, null=True)
    telefono_2 = models.CharField(max_length=1000, blank=True, null=True)
    cliente = models.CharField(max_length=1000, blank=True, null=True)
    apellido_p = models.CharField(max_length=1000, blank=True, null=True)
    apellido_m = models.CharField(max_length=1000, blank=True, null=True)
    dni = models.CharField(max_length=1000, blank=True, null=True)
    direccion = models.CharField(max_length=1000, blank=True, null=True)
    marca_vehiculo = models.CharField(max_length=1000, blank=True, null=True)
    modelo = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=1000, blank=True, null=True)
    cilindrada = models.CharField(max_length=1000, blank=True, null=True)
    kilometraje = models.CharField(max_length=1000, blank=True, null=True)
    placa = models.CharField(max_length=1000, blank=True, null=True)
    cantidad = models.CharField(max_length=1000, blank=True, null=True)
    marca_producto = models.CharField(max_length=1000, blank=True, null=True)
    modelo_bateria = models.CharField(max_length=1000, blank=True, null=True)
    precio = models.CharField(max_length=1000, blank=True, null=True)
    cantidad_bu = models.CharField(max_length=1000, blank=True, null=True)
    descuento = models.CharField(max_length=1000, blank=True, null=True)
    precio_total = models.CharField(max_length=1000, blank=True, null=True)
    fecha_atencion = models.DateField(blank=True, null=True)
    hora_instalacion = models.TimeField(blank=True, null=True)
    misma_direccion = models.CharField(max_length=1000, blank=True, null=True)
    direccion_atencion = models.CharField(max_length=1000, blank=True, null=True)
    referencia = models.CharField(max_length=1000, blank=True, null=True)
    boleta = models.IntegerField()
    mismo_cliente = models.CharField(max_length=1000, blank=True, null=True)
    nombre_boleta = models.CharField(max_length=1000, blank=True, null=True)
    m_apellido_p = models.CharField(max_length=1000, blank=True, null=True)
    m_apellido_m = models.CharField(max_length=1000, blank=True, null=True)
    dni_c = models.CharField(max_length=1000, blank=True, null=True)
    factura = models.IntegerField()
    ruc = models.CharField(max_length=1000, blank=True, null=True)
    razon_social = models.CharField(max_length=1000, blank=True, null=True)
    direccion_rs = models.CharField(max_length=1000, blank=True, null=True)
    correo = models.CharField(max_length=1000, blank=True, null=True)
    gmail = models.CharField(max_length=1000, blank=True, null=True)
    observaciones = models.CharField(max_length=1000, blank=True, null=True)
    almacen = models.ForeignKey(ColasinAlmacen, models.DO_NOTHING, blank=True, null=True)
    anio = models.ForeignKey(ColasinAnioV, models.DO_NOTHING, blank=True, null=True)
    atiende = models.ForeignKey(ColasinAtiende, models.DO_NOTHING, blank=True, null=True)
    color = models.ForeignKey(ColasinColoresV, models.DO_NOTHING, blank=True, null=True)
    distrito = models.ForeignKey(ColasinDistrito, models.DO_NOTHING, blank=True, null=True)
    pago = models.ForeignKey(ColasinPago, models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('ColasinStatus', models.DO_NOTHING, blank=True, null=True)
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    venta = models.ForeignKey('ColasinVenta', models.DO_NOTHING, blank=True, null=True)
    cierre = models.IntegerField()
    agente = models.ForeignKey(ColasinAgente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_produccion'


class ColasinProduccionaudio(models.Model):
    audio = models.CharField(max_length=1000, blank=True, null=True)
    produccion = models.ForeignKey(ColasinProduccion, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateTimeField()
    telefono = models.CharField(max_length=1000, blank=True, null=True)
    agente = models.ForeignKey(ColasinAgente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_produccionaudio'


class ColasinStatus(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_status'


class ColasinVehiculo(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)
    modelo = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colasIN_vehiculo'


class ColasinVenta(models.Model):
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'colasIN_venta'


class Comunica7Productos(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    prefijo = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunica7_productos'


class Comunica7Usuarios(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    distrito = models.CharField(max_length=100, blank=True, null=True)
    ruc = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunica7_usuarios'


class Comunica7UsuariosProductos(models.Model):
    usuario = models.ForeignKey(Comunica7Usuarios, models.DO_NOTHING, blank=True, null=True)
    producto = models.ForeignKey(Comunica7Productos, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunica7_usuarios_productos'


class DiscadorAgente(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    supervisor = models.CharField(max_length=100, blank=True, null=True)
    anexo = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    t_inicio_gestion = models.CharField(max_length=100, blank=True, null=True)
    t_fin_gestion = models.CharField(max_length=100, blank=True, null=True)
    t_inicio_llamada = models.CharField(max_length=100, blank=True, null=True)
    t_fin_llamada = models.CharField(max_length=100, blank=True, null=True)
    t_inicio_espera = models.CharField(max_length=100, blank=True, null=True)
    t_fin_espera = models.CharField(max_length=100, blank=True, null=True)
    contactadas = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_agente'


class DiscadorCartera(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_cartera'


class DiscadorCliente(models.Model):
    user = models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(max_length=100, blank=True, null=True)
    operacion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    tipo_persona = models.CharField(max_length=100, blank=True, null=True)
    tipo_documento = models.CharField(max_length=100, blank=True, null=True)
    numero_documento = models.CharField(max_length=100, blank=True, null=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_cliente'


class DiscadorCuadrante(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_cuadrante'


class DiscadorCuentas(models.Model):
    idcliente = models.CharField(max_length=100, blank=True, null=True)
    numero_cuenta = models.CharField(max_length=100, blank=True, null=True)
    moneda = models.CharField(max_length=100, blank=True, null=True)
    producto = models.CharField(max_length=100, blank=True, null=True)
    tipo_credito = models.CharField(max_length=100, blank=True, null=True)
    tipo_clasificacion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    fecha_vencimiento = models.CharField(max_length=100, blank=True, null=True)
    fecha_concecion = models.CharField(max_length=1000, blank=True, null=True)
    nuemero_cuotas = models.CharField(max_length=100, blank=True, null=True)
    dias_mora = models.CharField(max_length=100, blank=True, null=True)
    tramo = models.CharField(max_length=100, blank=True, null=True)
    rango_dias = models.CharField(max_length=100, blank=True, null=True)
    segmento = models.CharField(max_length=100, blank=True, null=True)
    grupo = models.CharField(max_length=100, blank=True, null=True)
    ciclo = models.CharField(max_length=100, blank=True, null=True)
    imp_capital = models.CharField(max_length=100, blank=True, null=True)
    imp_interes = models.CharField(max_length=100, blank=True, null=True)
    imp_mora = models.CharField(max_length=100, blank=True, null=True)
    imp_otros = models.CharField(max_length=100, blank=True, null=True)
    imp_total = models.CharField(max_length=100, blank=True, null=True)
    imp_vencido = models.CharField(max_length=100, blank=True, null=True)
    imp_minimo = models.CharField(max_length=100, blank=True, null=True)
    imp_descuento = models.CharField(max_length=100, blank=True, null=True)
    imp_campania = models.CharField(max_length=100, blank=True, null=True)
    imp_cap_original = models.CharField(max_length=100, blank=True, null=True)
    imp_prox_pago = models.CharField(max_length=100, blank=True, null=True)
    fecha_prox_pago = models.CharField(max_length=100, blank=True, null=True)
    observacion01 = models.CharField(max_length=100, blank=True, null=True)
    observacion02 = models.CharField(max_length=100, blank=True, null=True)
    observacion03 = models.CharField(max_length=100, blank=True, null=True)
    nro_tarjeta = models.CharField(max_length=100, blank=True, null=True)
    fecha_deuda = models.CharField(max_length=100, blank=True, null=True)
    id_gestor = models.CharField(max_length=100, blank=True, null=True)
    cartera = models.ForeignKey(DiscadorCartera, models.DO_NOTHING, blank=True, null=True)
    cliente = models.ForeignKey(DiscadorCliente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_cuentas'


class DiscadorDirecciones(models.Model):
    ubigeo = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    plano = models.CharField(max_length=100, blank=True, null=True)
    cuadrante = models.CharField(max_length=100, blank=True, null=True)
    fuente = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    cliente = models.ForeignKey(DiscadorCliente, models.DO_NOTHING, blank=True, null=True)
    tipo_direccion = models.ForeignKey('DiscadorTipoDireccion', models.DO_NOTHING, blank=True, null=True)
    tipo_domicilio = models.ForeignKey('DiscadorTipoDomicilio', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_direcciones'


class DiscadorEstadoCliente(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_estado_cliente'


class DiscadorEstadoscore(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_estadoscore'


class DiscadorFuenteTelefono(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_fuente_telefono'


class DiscadorGestion(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_gestion'


class DiscadorIdgestion(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_idgestion'


class DiscadorIndustria(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_industria'


class DiscadorMail(models.Model):
    correo = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    fuente = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    cliente = models.ForeignKey(DiscadorCliente, models.DO_NOTHING, blank=True, null=True)
    tipo_contacto = models.ForeignKey('DiscadorTipoContacto', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_mail'


class DiscadorNegocio(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_negocio'


class DiscadorPlano(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_plano'


class DiscadorProducto(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_producto'


class DiscadorProveedor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    industria = models.ForeignKey(DiscadorIndustria, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_proveedor'


class DiscadorProveedorcarteras(models.Model):
    cartera = models.ForeignKey(DiscadorCartera, models.DO_NOTHING, blank=True, null=True)
    negocio = models.ForeignKey(DiscadorNegocio, models.DO_NOTHING, blank=True, null=True)
    proveedor = models.ForeignKey(DiscadorProveedor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_proveedorcarteras'


class DiscadorResultado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_resultado'


class DiscadorScore(models.Model):
    peso_tipo_gestion = models.CharField(max_length=1)
    peso_id_gestion = models.CharField(max_length=1)
    peso_resultado = models.CharField(max_length=1)
    peso_subresultado = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=1)
    gestion = models.ForeignKey(DiscadorGestion, models.DO_NOTHING, blank=True, null=True)
    id_gestion = models.ForeignKey(DiscadorIdgestion, models.DO_NOTHING, blank=True, null=True)
    negocio = models.ForeignKey(DiscadorNegocio, models.DO_NOTHING, blank=True, null=True)
    resultado = models.ForeignKey(DiscadorResultado, models.DO_NOTHING, blank=True, null=True)
    subresultado = models.ForeignKey('DiscadorSubresultado', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discador_score'


class DiscadorScoreproveedor(models.Model):
    peso_tipo_gestion = models.CharField(max_length=1)
    peso_id_gestion = models.CharField(max_length=1)
    peso_resultado = models.CharField(max_length=1)
    peso_subresultado = models.CharField(max_length=1)
    estado = models.CharField(max_length=1)
    cartera = models.ForeignKey(DiscadorCartera, models.DO_NOTHING, blank=True, null=True)
    gestion = models.ForeignKey(DiscadorGestion, models.DO_NOTHING, blank=True, null=True)
    id_gestion = models.ForeignKey(DiscadorIdgestion, models.DO_NOTHING, blank=True, null=True)
    negocio = models.ForeignKey(DiscadorNegocio, models.DO_NOTHING, blank=True, null=True)
    proveedor = models.ForeignKey(DiscadorProveedor, models.DO_NOTHING, blank=True, null=True)
    resultado = models.ForeignKey(DiscadorResultado, models.DO_NOTHING, blank=True, null=True)
    subresultado = models.ForeignKey('DiscadorSubresultado', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discador_scoreproveedor'


class DiscadorSegmentacion(models.Model):
    telefono = models.CharField(max_length=100, blank=True, null=True)
    orden = models.CharField(max_length=100, blank=True, null=True)
    cliente = models.CharField(max_length=100, blank=True, null=True)
    base = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_segmentacion'


class DiscadorSexo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_sexo'


class DiscadorSubresultado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_subresultado'


class DiscadorTelefonos(models.Model):
    discado = models.CharField(max_length=100, blank=True, null=True)
    numero_telefono = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    tipo_contacto = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    cliente = models.CharField(max_length=100, blank=True, null=True)
    fuente_telefono = models.ForeignKey(DiscadorFuenteTelefono, models.DO_NOTHING, blank=True, null=True)
    numero_documento = models.ForeignKey(DiscadorCliente, models.DO_NOTHING, blank=True, null=True)
    tipo_telefono = models.ForeignKey('DiscadorTipoTelefono', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_telefonos'


class DiscadorTipoCartera(models.Model):
    cod_dpto = models.CharField(max_length=100, blank=True, null=True)
    cod_prov = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    dpto = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    distrito = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_tipo_cartera'


class DiscadorTipoContacto(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_tipo_contacto'


class DiscadorTipoDireccion(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_tipo_direccion'


class DiscadorTipoDomicilio(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_tipo_domicilio'


class DiscadorTipoPersona(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_tipo_persona'


class DiscadorTipoTelefono(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_tipo_telefono'


class DiscadorUbigeo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discador_ubigeo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SpeechAgente(models.Model):
    anexo = models.IntegerField(blank=True, null=True)
    fono = models.IntegerField(blank=True, null=True)
    destino = models.IntegerField(blank=True, null=True)
    duracion = models.TimeField(blank=True, null=True)
    atendidas = models.IntegerField(blank=True, null=True)
    contactadas = models.IntegerField(blank=True, null=True)
    est_ag_predictivo = models.IntegerField(blank=True, null=True)
    canal = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    estado = models.ForeignKey('SpeechEstado', models.DO_NOTHING, db_column='estado', blank=True, null=True)
    supervisor = models.ForeignKey('SpeechSupervisor', models.DO_NOTHING, db_column='supervisor', blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speech_agente'


class SpeechApi(models.Model):
    host = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    metodo = models.CharField(max_length=100, blank=True, null=True)
    header = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'speech_api'


class SpeechBase(models.Model):
    codigo = models.CharField(max_length=100, blank=True, null=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(max_length=100, blank=True, null=True)
    telefono_1 = models.CharField(max_length=100, blank=True, null=True)
    telefono_2 = models.CharField(max_length=100, blank=True, null=True)
    importe = models.CharField(max_length=100, blank=True, null=True)
    fecha_promesa = models.CharField(max_length=100, blank=True, null=True)
    deuda = models.CharField(max_length=100, blank=True, null=True)
    deuda_pendiente = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField()
    campania = models.ForeignKey('SpeechCampania', models.DO_NOTHING, db_column='campania', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speech_base'


class SpeechCampania(models.Model):
    fecha_cargada = models.DateTimeField(db_column='fecha cargada')  # Field renamed to remove unsuitable characters.
    archivo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    cliente = models.ForeignKey('SpeechCliente', models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    estado = models.ForeignKey('SpeechEstadocampania', models.DO_NOTHING, db_column='estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speech_campania'


class SpeechCliente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'speech_cliente'


class SpeechDBlaster(models.Model):
    id_d_blaster = models.AutoField(primary_key=True)
    uid = models.CharField(db_column='UID', max_length=45)  # Field name made lowercase.
    fh_inicio = models.DateTimeField(db_column='FH_inicio', blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(max_length=20)
    parametro_1 = models.CharField(max_length=20)
    parametro_2 = models.CharField(max_length=20)
    parametro_3 = models.CharField(max_length=20)
    audio = models.CharField(max_length=200)
    audio2 = models.CharField(max_length=200)
    derivacion = models.CharField(max_length=200)
    lestado = models.IntegerField(db_column='lEstado', blank=True, null=True)  # Field name made lowercase.
    respuesta = models.IntegerField(blank=True, null=True)
    dtmf = models.IntegerField(blank=True, null=True)
    despedida = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    oc7_1 = models.IntegerField(db_column='OC7_1', blank=True, null=True)  # Field name made lowercase.
    oc7_2 = models.IntegerField(db_column='OC7_2', blank=True, null=True)  # Field name made lowercase.
    oc7_3 = models.CharField(db_column='OC7_3', max_length=10)  # Field name made lowercase.
    tduracion_ini = models.DateTimeField(db_column='tDuracion_ini', blank=True, null=True)  # Field name made lowercase.
    tduracion_fin = models.DateTimeField(db_column='tDuracion_fin', blank=True, null=True)  # Field name made lowercase.
    tduracion = models.IntegerField(db_column='tDuracion', blank=True, null=True)  # Field name made lowercase.
    vclient = models.IntegerField(blank=True, null=True)
    cid = models.CharField(max_length=45)
    evento = models.ForeignKey(SpeechCampania, models.DO_NOTHING, db_column='evento', blank=True, null=True)
    cliente = models.ForeignKey(SpeechCliente, models.DO_NOTHING, db_column='cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speech_d_blaster'


class SpeechDLlamadas(models.Model):
    id_d_llamadas = models.IntegerField(primary_key=True)
    cliente = models.CharField(max_length=45)
    uid = models.CharField(db_column='UID', max_length=45)  # Field name made lowercase.
    destino = models.CharField(max_length=20)
    audio = models.CharField(max_length=200)
    audio2 = models.CharField(max_length=200)
    derivacion = models.CharField(max_length=200)
    dtmf = models.IntegerField()
    despedida = models.IntegerField()
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45)
    llam_tipo = models.IntegerField(blank=True, null=True)
    llam_canal = models.CharField(max_length=100)
    llam_estado = models.IntegerField(blank=True, null=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True)  # Field name made lowercase.
    t_ins = models.DateTimeField(db_column='T_INS')  # Field name made lowercase.
    t_pro = models.DateTimeField(db_column='T_PRO')  # Field name made lowercase.
    t_res = models.DateTimeField(db_column='T_RES')  # Field name made lowercase.
    t_fin1 = models.DateTimeField(db_column='T_FIN1')  # Field name made lowercase.
    t_fin2 = models.DateTimeField(db_column='T_FIN2')  # Field name made lowercase.
    d_timbrado = models.IntegerField()
    d_ivr = models.IntegerField()
    d_respuesta = models.IntegerField()
    d_total = models.IntegerField()
    respuesta01 = models.IntegerField(db_column='Respuesta01')  # Field name made lowercase.
    respuesta02 = models.IntegerField(db_column='Respuesta02')  # Field name made lowercase.
    codcorte = models.IntegerField(db_column='CodCorte')  # Field name made lowercase.
    vuelta = models.IntegerField()
    vclient = models.IntegerField(blank=True, null=True)
    cid = models.CharField(max_length=45)
    resultado = models.CharField(max_length=200)
    id_d_blaster = models.ForeignKey(SpeechDBlaster, models.DO_NOTHING, db_column='id_d_blaster', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speech_d_llamadas'


class SpeechEstado(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'speech_estado'


class SpeechEstadocampania(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'speech_estadocampania'


class SpeechSupervisor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speech_supervisor'
