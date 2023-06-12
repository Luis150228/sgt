SELECT CONCAT('[', GROUP_CONCAT(
    CONCAT(
        '{"noe":"', COALESCE(noe, ''), 
        '", "num_pedido":"', COALESCE(num_pedido, ''), 
        '", "npvr":"', COALESCE(npvr, ''), 
        '", "idequipo":"', COALESCE(idequipo, ''), 
        '", "cantidad":"', COALESCE(cantidad, ''), 
        '", "f_entrada":"', COALESCE(f_entrada, ''), 
        '", "almacen":"', COALESCE(almacen, ''), 
        '", "motivo":"', COALESCE(motivo, ''), 
        '", "documentacion":"', COALESCE(documentacion, ''), 
        '", "observaciones":"', COALESCE(observaciones, ''), 
        '", "usr_registro":"', COALESCE(usr_registro, ''), 
        '", "f_registro":"', COALESCE(f_registro, ''), 
        '", "usr_modifica":"', COALESCE(usr_modifica, ''), 
        '", "f_modifica":"', COALESCE(f_modifica, ''), 
        '"}'
    )
), ']') AS data_json
FROM eut_hardware.almacen_ordenentrada;
