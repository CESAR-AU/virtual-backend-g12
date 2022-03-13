-- JOINS
USE prueba;

SELECT * 
FROM VACUNATORIOS INNER JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id = 9;

SELECT * 
FROM VACUNATORIOS LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id = 9;

SELECT * 
FROM VACUNATORIOS RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id = 9;

INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
                        ('POST JORGE GALVEZ', 15.121, -30.121, 'AV EL SOL 755', 'LUN-VIE 07:00 - 15:00', null, null);
                        
SELECT vacn.*, vacu.*
FROM VACUNATORIOS AS vacn
LEFT JOIN vacunas AS vacu ON vacn.vacuna_id = vacu.id
WHERE vacu.nombre = 'pfizer';

-- 1. Devolver todos los vacunatorio en los cuales la vacuna sea Sinopharm y su horario de atencion sea de LUN-VIE
SELECT van.*, vacu.* 
FROM vacunatorios van INNER JOIN vacunas vacu on van.vacuna_id = vacu.id
WHERE vacu.nombre = 'Sinopharm' AND (van.horario_atencion = 'LUN-VIE' OR van.horario_atencion = 'LUN-SAB' OR van.horario_atencion = 'LUN-MIE');
-- 2. Devolver solamente las vacunas cuyo vacunatorio este ubicado entre la latitud -5.00 y 10.00 IN()
SELECT van.*, vacu.* 
FROM vacunatorios van INNER JOIN vacunas vacu on van.vacuna_id = vacu.id
WHERE van.latitud BETWEEN -5 AND 10;
-- 3. Devolver todas las vacunas que no tengan vacunatorio y solamente su procedencia y nombre
SELECT vacu.nombre, vacu.procedencia
FROM vacunatorios van RIGHT JOIN vacunas vacu on van.vacuna_id = vacu.id
WHERE van.vacuna_id IS NULL