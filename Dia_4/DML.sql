USE prueba;
INSERT INTO clientes (nombre, documento, tipo_documento, estado) 
VALUES 
('Rosa', '25954514', 'DNI', true),
('Estefani', '10256548589', 'RUC', true),
('Fabian', '25659585', 'DNI', false);


SELECT * FROM clientes;
SELECT * FROM clientes WHERE documento = '25954514' AND (nombre = '' OR nombre = 'Rosa');
SELECT * FROM clientes WHERE tipo_documento = 'DNI' AND estado = true;
SELECT * FROM clientes WHERE nombre LIKE '%Ju%';
SELECT * FROM clientes WHERE nombre LIKE 'Ju%o';

UPDATE clientes SET nombre = 'JUAN', documento = '12345678' WHERE id = 1;

DELETE FROM clientes WHERE id = 2
