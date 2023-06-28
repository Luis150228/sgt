CREATE DEFINER=`lrangel`@`%` PROCEDURE `stp_addIncidents`(var_number VARCHAR(16), var_folio VARCHAR(16), var_sys_created_on DATETIME, var_work_end DATETIME, var_closed_at DATETIME, var_closed_by VARCHAR(250), var_assignment_group VARCHAR(250), var_assigned_to VARCHAR(250), var_state VARCHAR(250), var_category VARCHAR(250), var_subcategory VARCHAR(250), var_u_short_description_call VARCHAR(250), var_u_request_type VARCHAR(250), var_short_description MEDIUMTEXT, var_made_sla VARCHAR(12), var_u_zone VARCHAR(12), var_location VARCHAR(250), var_caller_id VARCHAR(250), var_sys_updated_by VARCHAR(250), var_calendar_duration VARCHAR(250), var_business_duration VARCHAR(250), var_company VARCHAR(250), var_description LONGTEXT, var_comments_and_work_notes LONGTEXT, var_opened_by VARCHAR(250), var_resolved_by VARCHAR(250), var_close_code VARCHAR(250), var_parent_incident VARCHAR(12), var_child_incidents VARCHAR(12), var_sys_updated_on DATETIME, var_sys_created_by VARCHAR(250), var_order_update DATETIME)
BEGIN


DECLARE folioExist INT;
DECLARE folioActualizado INT;
DECLARE dateActualizado DATETIME;
DECLARE let_u_zone INT;

call stp_addPromedios();/*Actualiza las bases para determinar dias inhabiles*/
SET folioExist = (SELECT COUNT(folio) FROM `servicenow` WHERE `folio` = var_folio);
/*SET folioActualizado = (SELECT COUNT(folio) FROM `servicenow` WHERE `folio` = var_folio and `actualizado` = var_sys_updated_on);*/
SET let_u_zone = (IF(var_u_zone = '', SUBSTRING_INDEX(SUBSTRING_INDEX(var_assignment_group, 'Zona_', -1), '_', 1), var_u_zone));

IF folioExist = 0 THEN
	INSERT INTO `servicenow` (`folio`,`abierto`,`resuelto`,`cerrado`,`creado_por`,`grup_asig`,`asig_a`,`estatus`, `solucion`, `categoria`,`subcategoria`,`subcategoria2`,`tipoproblema`,`nombreproyecto`,`sla`,`zona_num`,`ubicacion`,`abierto_por`,`solicitante`,`duracion`,`duracion_negocio`,`empresa`,`descripcion`,`obs_notasresolucion`,`cerrado_por`,`resuelto_por`,`codigo_cierre`,`incidencia_principal`,`incidencia_secundarias`,`actualizado`,`mail_creador`, `limitadores`, `suc_corp`, `origen`, `ceco`) VALUES (var_folio, var_sys_created_on, var_work_end, var_closed_at, var_closed_by, var_assignment_group, var_assigned_to, var_state, fn_estatus(var_state), var_category, var_subcategory, var_u_short_description_call, var_u_request_type, var_short_description, var_made_sla, let_u_zone, var_location, var_caller_id, var_sys_updated_by, var_calendar_duration, var_business_duration, var_company, var_description, var_comments_and_work_notes, var_opened_by, var_resolved_by, var_close_code, var_parent_incident, var_child_incidents, var_sys_updated_on, var_sys_created_by, fn_ks(var_comments_and_work_notes), fn_suc_corp(var_location), 'SNGlobal Incidentes', fn_cecoINC('0', var_location, var_comments_and_work_notes));
/*ELSEIF folioExist = 1 && folioActualizado = 0 THEN*/
ELSEIF folioExist = 1 THEN
	UPDATE `servicenow` SET `abierto` = var_sys_created_on,`resuelto` = var_work_end,`cerrado` = var_closed_at,`creado_por` = var_closed_by,`grup_asig` = var_assignment_group,`asig_a` = var_assigned_to,`estatus` = var_state, `solucion` = fn_estatus(var_state), `categoria` = var_category,`subcategoria` = var_subcategory,`subcategoria2` = var_u_short_description_call,`tipoproblema` = var_u_request_type,`nombreproyecto` = var_short_description,`sla` = var_made_sla, `zona_num` = let_u_zone,`ubicacion` = var_location,`abierto_por` = var_caller_id,`solicitante` = var_sys_updated_by,`duracion` = var_calendar_duration,`duracion_negocio` = var_business_duration,`empresa` = var_company,`descripcion` = var_description, `obs_notasresolucion` = var_comments_and_work_notes,`cerrado_por` = var_opened_by,`resuelto_por` = var_resolved_by,`codigo_cierre` = var_close_code,`incidencia_principal` = var_parent_incident,`incidencia_secundarias` = var_child_incidents,`actualizado` = var_sys_updated_on, `mail_creador` = var_sys_created_by, `limitadores` = fn_ks(var_comments_and_work_notes), `suc_corp` = fn_suc_corp(var_location), `origen` = 'SNGlobal Incidentes', `ceco` = fn_cecoINC('0', var_location, var_comments_and_work_notes) WHERE `folio` = var_folio;
END IF;

SET dateActualizado = (SELECT ifnull(max(actualizado), NOW()) FROM `servicenow` WHERE `f_alta` >= var_order_update and LEFT(`folio`, 3) = 'INC');
UPDATE `edodatabase` SET `dbUpdate` = dateActualizado WHERE (`id` >= 0) AND `nombre` = 'incidentes';

SELECT COUNT(*) as 'total', max(`actualizado`) as 'actualizado' FROM `servicenow` WHERE `f_alta` >= var_order_update and LEFT(`folio`, 3) = 'INC';

END
