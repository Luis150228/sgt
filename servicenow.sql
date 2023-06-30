SELECT
  grupo,
  SUBSTRING_INDEX(SUBSTRING_INDEX(grupo, 'Zona_', -1), '_', 1) AS numero_zona
FROM
  tu_tabla
WHERE
  grupo REGEXP 'Zona_[0-4]';

SELECT GREATEST(columna1, columna2, columna3) AS fecha_maxima
FROM tu_tabla;

SELECT SUBSTRING(LEFT(tu_columna, 20), 1, 20) AS primeros_20_digitos
FROM tu_tabla;
