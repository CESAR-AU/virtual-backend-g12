USE colegio;
-- 1. Todas los alumnos que tienen correo GMAIL
SELECT * FROM tbl_alumnos 
WHERE correo LIKE '%GMAIL.COM';
-- 2. Todos los alumnos (nombre, ap_pat, ap_mat) que hayan curso en el 2002
SELECT TA.* FROM tbl_alumnos  TA INNER JOIN tbl_alumnos_niveles TAN ON TAN.alumnos_id = TA.id
WHERE TAN.fecha_cursada = 2022;
-- 3. Todos los grados donde su ubicacion sea el sotano o segundo piso
SELECT * FROM tbl_niveles 
WHERE ubicacion = 'sotano' OR ubicacion = 'segundo piso';
-- 4. Todos los grados (Seccion y el nombre ) que han tenidos alumnos en el año 2003
SELECT TN.* FROM tbl_niveles  TN INNER JOIN tbl_alumnos_niveles TAN ON TAN.nivel_id = TN.id
WHERE TAN.fecha_cursada = 2003;
-- NOTA: si no tienen esas secciones usar secciones que si tengan
-- 5. Mostrar todos los alumnos del quinto A
SELECT TA.*, TAN.fecha_cursada, TN.nombre AS nombre_nivel, TN.seccion, TN.ubicacion 
FROM tbl_alumnos TA 
INNER JOIN tbl_alumnos_niveles TAN ON TAN.alumnos_id = TA.id
INNER JOIN tbl_niveles TN ON TAN.nivel_id = TN.id
WHERE /*TAN.fecha_cursada = 2000 AND*/ TN.seccion = 'A' AND TN.nombre LIKE 'quinto';

-- 6. Mostrar todos los correos de los alumnos del primero B 
SELECT TA.correo
FROM tbl_alumnos TA 
LEFT JOIN tbl_alumnos_niveles TAN ON TAN.alumnos_id = TA.id
LEFT JOIN tbl_niveles TN ON TAN.nivel_id = TN.id
WHERE /*TAN.fecha_cursada = 2022 AND */ TN.seccion = 'B' AND TN.nombre LIKE 'primero'

