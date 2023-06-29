tengo el siguiente procedimiento almacenado y al usarlo da el error se da cuando quiero actualizar la siguiente tabla y como puedes ver el  PRIMARY KEY (`folio`) USING BTREE, que es justo lo que uso como parametro del where cuanto quiero actualiar `servicenow_reportes`
por que se esta dando el error si uso la KEY column para modificar el registro??????????

CREATE DEFINER=`lrangel`@`%` PROCEDURE `stp_addIncidents`(var_number VARCHAR(16), var_folio VARCHAR(16), var_sys_created_on DATETIME, var_work_end DATETIME, var_closed_at DATETIME, var_closed_by VARCHAR(250), var_assignment_group VARCHAR(250), var_assigned_to VARCHAR(250), var_state VARCHAR(250), var_category VARCHAR(250), var_subcategory VARCHAR(250), var_u_short_description_call VARCHAR(250), var_u_request_type VARCHAR(250), var_short_description MEDIUMTEXT, var_made_sla VARCHAR(12), var_u_zone VARCHAR(12), var_location VARCHAR(250), var_caller_id VARCHAR(250), var_sys_updated_by VARCHAR(250), var_calendar_duration VARCHAR(250), var_business_duration VARCHAR(250), var_company VARCHAR(250), var_description LONGTEXT, var_comments_and_work_notes LONGTEXT, var_opened_by VARCHAR(250), var_resolved_by VARCHAR(250), var_close_code VARCHAR(250), var_parent_incident VARCHAR(12), var_child_incidents VARCHAR(12), var_sys_updated_on DATETIME, var_sys_created_by VARCHAR(250), var_order_update DATETIME)
BEGIN


DECLARE folioExist INT;
DECLARE folioActualizado INT;
DECLARE dateActualizado DATETIME;
DECLARE let_u_zone INT;

call stp_addPromedios();/*Actualiza las bases para determinar dias inhabiles*/
SET folioExist = (SELECT COUNT(folio) FROM `servicenow_reportes` WHERE `folio` = var_folio);
SET let_u_zone = (IF(var_u_zone = '', SUBSTRING_INDEX(SUBSTRING_INDEX(var_assignment_group, 'Zona_', -1), '_', 1), var_u_zone));

IF folioExist = 0 THEN
	INSERT INTO `servicenow_reportes` (`folio`,`abierto`,`resuelto`,`cerrado`,`creado_por`,`grup_asig`,`asig_a`,`estatus`, `solucion`, `categoria`,`subcategoria`,`subcategoria2`,`tipoproblema`,`nombreproyecto`,`sla`,`zona_num`,`ubicacion`,`abierto_por`,`solicitante`,`duracion`,`duracion_negocio`,`empresa`,`descripcion`,`obs_notasresolucion`,`cerrado_por`,`resuelto_por`,`codigo_cierre`,`incidencia_principal`,`incidencia_secundarias`,`actualizado`,`mail_creador`, `limitadores`, `suc_corp`, `origen`, `ceco`) VALUES (var_folio, var_sys_created_on, var_work_end, var_closed_at, var_closed_by, var_assignment_group, var_assigned_to, var_state, fn_estatus(var_state), var_category, var_subcategory, var_u_short_description_call, var_u_request_type, var_short_description, var_made_sla, let_u_zone, var_location, var_caller_id, var_sys_updated_by, var_calendar_duration, var_business_duration, var_company, var_description, var_comments_and_work_notes, var_opened_by, var_resolved_by, var_close_code, var_parent_incident, var_child_incidents, var_sys_updated_on, var_sys_created_by, fn_ks(var_comments_and_work_notes), fn_suc_corp(var_location), 'SNGlobal Incidentes', fn_cecoINC('0', var_location, var_comments_and_work_notes));
ELSEIF folioExist = 1 THEN
	UPDATE `servicenow_reportes` SET `resuelto` = var_work_end, `cerrado` = var_closed_at, `grup_asig` = var_assignment_group, `asig_a` = var_assigned_to, `estatus` = var_state, `solucion` = fn_estatus(var_state), `zona_num` = let_u_zone, `descripcion` = var_description, `obs_notasresolucion` = var_comments_and_work_notes, `cerrado_por` = var_opened_by, `resuelto_por` = var_resolved_by, `codigo_cierre` = var_close_code, `incidencia_principal` = var_parent_incident, `incidencia_secundarias` = var_child_incidents,`actualizado` = var_sys_updated_on, `limitadores` = fn_ks(var_comments_and_work_notes), `suc_corp` = fn_suc_corp(var_location), `origen` = 'SNGlobal Incidentes', `ceco` = fn_cecoINC('0', var_location, var_comments_and_work_notes) WHERE `folio` = var_folio;
END IF;

SET dateActualizado = (SELECT max(actualizado) FROM `servicenow_reportes` WHERE LEFT(`folio`, 3) = 'INC');
UPDATE `edodatabase` SET `dbUpdate` = dateActualizado WHERE (`id` >= 0) AND `nombre` = 'incidentes';

SELECT COUNT(*) as 'total', max(`actualizado`) as 'actualizado' FROM `servicenow_reportes` WHERE LEFT(`folio`, 3) = 'INC';

END

	
CALL stp_addIncidents('035317965','INC035317965','2023-06-23 19:30:40','2023-06-23 19:36:36','','','TMX_EU_Resolutores_SDK_Zona_0','JOHANNY HERNANDEZ RENDON','Resuelto','Software Usuario Final','Software','Falla Navegador','Aplicación','Reportes de Navegadores (Microsoft Edge, Google Chrome)','true','0','EDIF. CORPORATIVO SANTA FE','JANETTE FIGUEROA CORREA','Z412404@santandertec.mx','357','357','Santander México','Variables: Tipo de Falla: Otro. Correo Electrónico: jfigueroac@santander.com.mx Extensión: 5548817205 Celular: 554/881-7205 Extensión de Segundo Contacto: 5548817205 Especifique en que momento o al hacer que aparece el error: No se pueden generar contraseñas de dominio Sector/Modulo/Piso: OFNA CORPORATIVO STA FE CDMX_GSM Departamento: SD Gestion Operativa Entidad: Corporativo Expediente: 805971 Segundo Contacto: FIGUEROA CORREA JANETTE Último Acceso Exitoso: Un Día Teléfono: 554/881-7205 Describa de manera clara la Solicitud o Falla que está reportando.: no marca error el IVR pero están registrándose como desbloqueo fallido. ','2023-06-23 19:36:36 - JOHANNY HERNANDEZ RENDON (Notas de trabajo) **NO SE REALIZA CONEXION REMOTA** FALLA REAL: PROBLEMAS CON IVR DESBLOQUEOS DOMINIO VO.BO:FIGUEROA CORREA JANETTE ING:JOHANNY HERNANDEZ RENDON SOLUCION:SE GENERA CONTRASEÑA Y VALIDA SU ACCESO DE FORMA CORRECTA ZONA: TMX_EU_Resolutores_SDK_Zona_0 CC: N/A SUC/CORP:EDIF. CORPORATIVO SANTA FE VERSION DE SO:20H2 Versión SDK Click: 2.0 Dominio:GFSSCORP 2023-06-23 19:36:36 - JOHANNY HERNANDEZ RENDON (Notas de trabajo) Resolution has been modified in service Now to: Request Type: Aplicación Resolution Type: Soporte Técnico Resolution Code: Solucionado (de forma permanente) Resolution notes: **NO SE REALIZA CONEXION REMOTA** FALLA REAL: PROBLEMAS CON IVR DESBLOQUEOS DOMINIO VO.BO:FIGUEROA CORREA JANETTE ING:JOHANNY HERNANDEZ RENDON SOLUCION:SE GENERA CONTRASEÑA Y VALIDA SU ACCESO DE FORMA CORRECTA ZONA: TMX_EU_Resolutores_SDK_Zona_0 CC: N/A SUC/CORP:EDIF. CORPORATIVO SANTA FE VERSION DE SO:20H2 Versión SDK Click: 2.0 Dominio:GFSSCORP 2023-06-23 19:36:36 - JOHANNY HERNANDEZ RENDON (Observaciones adicionales) Notas de resolución: **NO SE REALIZA CONEXION REMOTA** FALLA REAL: PROBLEMAS CON IVR DESBLOQUEOS DOMINIO VO.BO:FIGUEROA CORREA JANETTE ING:JOHANNY HERNANDEZ RENDON SOLUCION:SE GENERA CONTRASEÑA Y VALIDA SU ACCESO DE FORMA CORRECTA ZONA: TMX_EU_Resolutores_SDK_Zona_0 CC: N/A SUC/CORP:EDIF. CORPORATIVO SANTA FE VERSION DE SO:20H2 Versión SDK Click: 2.0 Dominio:GFSSCORP ','JOHANNY HERNANDEZ RENDON','JOHANNY HERNANDEZ RENDON','Solucionado (de forma permanente)','INC035139185','0','2023-06-23 19:36:36','Z412404@santandertec.mx"','2023-06-28 17:20:41');

Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.

CREATE TABLE `servicenow_reportes` (
  `folio` varchar(20) NOT NULL,
  `abierto` datetime DEFAULT NULL,
  `resuelto` datetime DEFAULT NULL,
  `cerrado` datetime DEFAULT NULL,
  `creado_por` varchar(250) DEFAULT NULL,
  `grup_asig` varchar(150) DEFAULT NULL,
  `asig_a` varchar(150) DEFAULT NULL,
  `estatus` varchar(20) DEFAULT NULL,
  `categoria` varchar(150) DEFAULT NULL,
  `subcategoria` varchar(150) DEFAULT NULL,
  `subcategoria2` varchar(120) DEFAULT NULL,
  `tipoproblema` varchar(120) DEFAULT NULL,
  `nombreproyecto` varchar(150) DEFAULT NULL,
  `sla` int(4) DEFAULT NULL,
  `ceco` int(4) DEFAULT NULL,
  `ubicacion` varchar(150) DEFAULT NULL,
  `abierto_por` varchar(150) DEFAULT NULL,
  `solicitante` varchar(150) DEFAULT NULL,
  `duracion` int(11) DEFAULT NULL,
  `duracion_negocio` int(11) DEFAULT NULL,
  `empresa` varchar(150) DEFAULT NULL,
  `descripcion` mediumtext DEFAULT NULL,
  `obs_notasresolucion` longtext DEFAULT NULL,
  `cerrado_por` varchar(150) DEFAULT NULL,
  `resuelto_por` varchar(150) DEFAULT NULL,
  `codigo_cierre` varchar(150) DEFAULT NULL,
  `incidencia_principal` varchar(45) DEFAULT NULL,
  `incidencia_secundarias` varchar(45) DEFAULT NULL,
  `actualizado` datetime DEFAULT NULL,
  `mail_creador` varchar(150) DEFAULT NULL,
  `id_ext` varchar(50) DEFAULT NULL,
  `clasificacion` varchar(50) DEFAULT NULL,
  `aplicativo` varchar(50) DEFAULT NULL,
  `plataforma` varchar(50) DEFAULT NULL,
  `falla` varchar(50) DEFAULT NULL,
  `solucion` varchar(50) DEFAULT NULL,
  `causa_raiz` varchar(50) DEFAULT NULL,
  `useralta` varchar(20) DEFAULT NULL,
  `limitadores` varchar(4) DEFAULT NULL,
  `tiempo` int(5) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `zona_ubica` varchar(50) DEFAULT NULL,
  `zona_num` int(1) DEFAULT NULL,
  `region_cau` varchar(50) DEFAULT NULL,
  `sla_tsucursales` int(6) DEFAULT NULL,
  `grupo_gral` varchar(50) DEFAULT NULL,
  `grupo_local` varchar(50) DEFAULT NULL,
  `medido` varchar(50) DEFAULT NULL,
  `exc_user` varchar(7) DEFAULT NULL,
  `exc_obs` tinytext DEFAULT NULL,
  `exc_clave` varchar(250) DEFAULT NULL,
  `exc_region` varchar(145) DEFAULT NULL,
  `exc_metrica` varchar(20) DEFAULT NULL,
  `exc_status` varchar(150) DEFAULT 'En Metrica',
  `suc_corp` varchar(50) DEFAULT NULL,
  `sf_descrip_gral` varchar(150) DEFAULT NULL,
  `sf_descrip_especif` tinytext DEFAULT NULL,
  `id_fespecif` int(11) DEFAULT NULL,
  `sf_descrip_type` varchar(50) DEFAULT NULL,
  `sf_minutos` int(11) DEFAULT NULL,
  `semanal_rango` varchar(45) DEFAULT NULL,
  `semanal_mes` varchar(10) DEFAULT NULL,
  `tipos` varchar(45) DEFAULT NULL,
  `origen` varchar(25) DEFAULT NULL,
  `f_alta` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`folio`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
