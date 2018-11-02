curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "Authorization: Basic ZGlsb29kaXJlY3Q6ampVWTI2c1Q=" \
-d "{\"to\":[\"051980729169\"],\"text\":\"mensaje de texto\",\"from\":\"msg\"}" \
https://gateway.plusmms.net/rest/message 



redis-server /usr/local/etc/redis.conf

racle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show triggers;
ERROR 1046 (3D000): No database selected
mysql> use perucall;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show triggers;
+-----------------+--------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------+--------------------------------------------+----------------+----------------------+----------------------+--------------------+
| Trigger         | Event  | Table       | Statement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Timing | Created | sql_mode                                   | Definer        | character_set_client | collation_connection | Database Collation |
+-----------------+--------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------+--------------------------------------------+----------------+----------------------+----------------------+--------------------+
| replica         | INSERT | ajx_pro_acd | BEGIN
    INSERT INTO logPhon set
     logPhon.id_ori_usuario=NEW.id_ori_usuario,
     logPhon.id_ori_seg_cola=NEW.id_ori_campana,
     logPhon.duration=NEW.duration,
     logPhon.anexo=NEW.anexo,
     logPhon.espera=NEW.espera,
     logPhon.llam_estado=new.llam_estado,
     logPhon.id_ori_campana=NEW.id_ori_campana,
     logPhon.origen=NEW.Numero_Entrante,
     logPhon.destino=NEW.Numero_Llamado,
     logPhon.tipo_llamada=1,
     logPhon.audio=NEW.audio,
     logPhon.channel1=NEW.Channel_Entrante,
     logPhon.age_nombre=NEW.age_nombre,
     logPhon.tie_ing=NEW.tie_ing,
     logPhon.tie_acd=NEW.tie_acd,
     logPhon.tie_tra=NEW.tie_tra,
     logPhon.tie_con=NEW.tie_con,
     logPhon.tie_fin=NEW.tie_fin,
     logPhon.tie_acw=NEW.tie_acw,
     logPhon.flag=NEW.flag,
     logPhon.uniqueid=NEW.uniqueid,
     logPhon.fin=NEW.fin,
     logPhon.sql=NEW.sql,
     logPhon.codhu=NEW.CodHU,
     logPhon.bill=NEW.bill,
     logPhon.asterisk=NEW.asterisk,
     logPhon.valorllamada=NEW.valorllamada,
     logPhon.bk_id=NEW.id_ori_acd ;
  END | AFTER  | NULL    | NO_AUTO_VALUE_ON_ZERO                      | root@localhost | utf8                 | utf8_general_ci      | latin1_swedish_ci  |
| replica3        | UPDATE | ajx_pro_acd | BEGIN
    UPDATE logPhon SET
     logPhon.anexo=NEW.anexo,
     logPhon.duration=NEW.duration,
     logPhon.espera=NEW.espera,
     logPhon.llam_estado=new.llam_estado,
     logPhon.id_ori_usuario=NEW.id_ori_usuario,
     logPhon.id_ori_seg_cola=NEW.id_ori_campana,
     logPhon.id_ori_campana=NEW.id_ori_campana,
     logPhon.origen=NEW.Numero_Entrante,
     logPhon.destino=NEW.Numero_Llamado,
     logPhon.tipo_llamada=1,
     logPhon.audio=NEW.audio,
     logPhon.channel1=NEW.Channel_Entrante,
     logPhon.age_nombre=NEW.age_nombre,
     logPhon.tie_ing=NEW.tie_ing,
     logPhon.tie_acd=NEW.tie_acd,
     logPhon.tie_tra=NEW.tie_tra,
     logPhon.tie_con=NEW.tie_con,
     logPhon.tie_fin=NEW.tie_fin,
     logPhon.tie_acw=NEW.tie_acw,
     logPhon.flag=NEW.flag,
     logPhon.uniqueid=NEW.uniqueid,
     logPhon.fin=NEW.fin,
     logPhon.sql=NEW.sql,
     logPhon.codhu=NEW.CodHU,
     logPhon.bill=NEW.bill,
     logPhon.asterisk=NEW.asterisk,
     logPhon.valorllamada=NEW.valorllamada
   WHERE logPhon.bk_id = NEW.id_ori_acd and logPhon.tipo = 0;
  END | AFTER  | NULL    | NO_AUTO_VALUE_ON_ZERO                      | root@localhost | utf8                 | utf8_general_ci      | latin1_swedish_ci  |
| INSERTA_LLAMADA | INSERT | ajx_pro_lla | INSERT INTO misllamadas
   ( 
    id_ori_llamadas ,
    age_ip ,
    age_codigo ,
    cam_codigo,
    llam_numero ,
    llam_estado,
    llam_flag,
    llam_uniqueid ,
    tipo,
    f_origen ,
    canal1 ,
    canal2 ,
    channel ,
    dstchannel ,
    flagfin ,
    v_tring ,
    v_retry ,
    ring ,
    duration ,
    bill ,
    tregistro ,
    gestion_editid1 ,
    gestion_editid2 ,
    gestion_editid3 ,
    f_llam_fin ,
    f_llam_discador ,
    f_llam_resuelve ,
    id_ori_campana,
    id_cliente,
    coderr,
    coderr1 ,
    audio,
    audio2,
    gestion_editid4,
    gestion_editid5,
    gestion_editid6,
    gestion_editid7,
    gestion_editid8,
    gestion_editid9,
    gestion_editid10,
    dialstatus,
    dialstatus1,
    id_ori_seg_cola,
    age_nombre,
    anexo,
    espera,
    troncal ,
    timbrado1,
    timbrado2,
    prefijo ,
    grabacion,
    in_id,
    v_tipbusc
     )
   VALUES
   (  NEW.id_ori_llamadas ,
      NEW.age_ip ,
      NEW.age_codigo ,
      NEW.cam_codigo,
      NEW.llam_numero ,
      NEW.llam_estado,
      NEW.llam_flag,
      NEW.llam_uniqueid ,
      NEW.tipo,
      NEW.f_origen ,
      NEW.canal1 ,
      NEW.canal2 ,
      NEW.channel ,
      NEW.dstchannel ,
      NEW.flagfin ,
      NEW.v_tring ,
      NEW.v_retry ,
      NEW.ring ,
      NEW.duration ,
      NEW.bill ,
      NEW.tregistro ,
      NEW.gestion_editid1 ,
      NEW.gestion_editid2 ,
      NEW.gestion_editid3 ,
      NEW.f_llam_fin ,
      NEW.f_llam_discador ,
      NEW.f_llam_resuelve ,
      NEW.id_ori_campana,
      NEW.id_cliente,
      NEW.coderr,
      NEW.coderr1 ,
      NEW.audio,
      NEW.audio2,
      NEW.gestion_editid4,
      NEW.gestion_editid5,
      NEW.gestion_editid6,
      NEW.gestion_editid7,
      NEW.gestion_editid8,
      NEW.gestion_editid9,
      NEW.gestion_editid10,
      NEW.dialstatus,
      NEW.dialstatus1,
      NEW.id_ori_seg_cola,
      NEW.age_nombre,
      NEW.anexo,
      NEW.espera,
      NEW.troncal ,
      NEW.timbrado1,
      NEW.timbrado2,
      NEW.prefijo ,
      NEW.grabacion,
      NEW.in_id,
      NEW.v_tipbusc
 ) | AFTER  | NULL    | STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION | root@localhost | latin1               | latin1_swedish_ci    | latin1_swedish_ci  |
| UPDATE_LLAMADAS | UPDATE | ajx_pro_lla | UPDATE misllamadas set 
    
      age_ip = NEW.age_ip ,
      age_codigo = NEW.age_codigo ,
      cam_codigo= NEW.cam_codigo,
      llam_numero = NEW.llam_numero ,
      llam_estado= NEW.llam_estado,
      llam_flag= NEW.llam_flag,
      llam_uniqueid = NEW.llam_uniqueid ,
      tipo= NEW.tipo,
      f_origen = NEW.f_origen ,
      canal1 = NEW.canal1 ,
      canal2 = NEW.canal2 ,
      channel = NEW.channel ,
      dstchannel = NEW.dstchannel ,
      flagfin = NEW.flagfin ,
      v_tring = NEW.v_tring ,
      v_retry = NEW.v_retry ,
      ring = NEW.ring ,
      duration = NEW.duration ,
      bill = NEW.bill ,
      tregistro = NEW.tregistro ,
      gestion_editid1 = NEW.gestion_editid1 ,
      gestion_editid2 = NEW.gestion_editid2 ,
      gestion_editid3 = NEW.gestion_editid3 ,
      f_llam_fin = NEW.f_llam_fin ,
      f_llam_discador = NEW.f_llam_discador ,
      f_llam_resuelve = NEW.f_llam_resuelve ,
      id_ori_campana= NEW.id_ori_campana,
      id_cliente= NEW.id_cliente,
      coderr= NEW.coderr,
      coderr1 = NEW.coderr1 ,
      audio= NEW.audio,
      audio2= NEW.audio2,
      gestion_editid4= NEW.gestion_editid4,
      gestion_editid5= NEW.gestion_editid5,
      gestion_editid6= NEW.gestion_editid6,
      gestion_editid7= NEW.gestion_editid7,
      gestion_editid8= NEW.gestion_editid8,
      gestion_editid9= NEW.gestion_editid9,
      gestion_editid10= NEW.gestion_editid10,
      dialstatus= NEW.dialstatus,
      dialstatus1= NEW.dialstatus1,
      id_ori_seg_cola= NEW.id_ori_seg_cola,
      age_nombre= NEW.age_nombre,
      anexo= NEW.anexo,
      espera= NEW.espera,
      troncal = NEW.troncal ,
      timbrado1= NEW.timbrado1,
      timbrado2= NEW.timbrado2,
      prefijo = NEW.prefijo ,
      grabacion= NEW.grabacion,
      in_id= NEW.in_id


    where

    id_ori_llamadas=NEW.id_ori_llamadas | AFTER  | NULL    | STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION | root@localhost | latin1               | latin1_swedish_ci    | latin1_swedish_ci  |
+-----------------+--------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------+--------------------------------------------+----------------+----------------------+----------------------+--------------------+
4 rows in set (0.01 sec)