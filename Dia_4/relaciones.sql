CREATE TABLE vacunas(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) UNIQUE NOT NULL,
    estado BOOL DEFAULT true,
    fecha_vencimiento DATE,
    procedencia ENUM('USA', 'CHINA', 'RUSIA', 'UK'),
    lote VARCHAR(10)    
);

CREATE TABLE vacunatorio(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE NOT  NULL,
    latitud FLOAT,
    longitud FLOAT,
    direccion VARCHAR(250),
    horario_atencion VARCHAR(100),
    vacuna_id INT,
    FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
)

-- RENAME TABLE old TO new

-- ALTER TABLE vacunatorio ADD COLUMN imagen TEXT AFTER horario_atencion;
-- >  v8 ALTER TABLE vacunatorio RENAME COLUMN imagen TO foto;
-- < 5.7 ALTER TABLE vacunatorio CHANGE imagen  foto VARCHAR(100) DEFAULT 'img.png';
-- ALTER TABLE vacunatorio MODIFY COLUMN imagen VARCHAR(100);

-- DESC clientes;

USE prueba;
INSERT INTO vacunas (nombre, estado, fecha_vencimiento, procedencia, lote) VALUES 
('PFIZER', true, '2022-08-16', 'USA', '123-132'),
('SINOPHARM', true, '2022-10-10', 'CHINA', '123-545'),
('MODERNA', true, '2022-09-09', 'USA', '123-545'),
('SPUTNIK', false, '2022-10-04', 'RUSIA', '123-1354789');

INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
                        ('CAMINO REAL', 14.121, -21.121, 'AV GIRASOL 115', 'LUN-VIE 07:00 - 15:00', null, 9),
                        ('HOSP. GNRAL.', 17.521, 11.1891, 'AV CIRCUNVALACION S/N', 'LUN-VIE 07:00 - 15:00', 'hospital.jpg', 10),
                        ('POSTA CERRO AZUL', 11.258, 67.447, 'AAHH LOS QUERUBINES LOTE 3 MZ J', 'LUN-SAB 07:00 - 15:00', 'foto01.png', 9),
                        ('ESTADIO LOS PALITOS', 24.121, -21.121, 'CALLE ESPINOSA 1115', 'LUN-MIE-VIE 07:00 - 15:00', 'est0001.jpg', 11),
                        ('PLAZA DEL AMOR', 4.116, -21.121, 'AV DE LOS HEROES ANONIMOS S/N', 'LUN-VIE 07:00 - 15:00', null, 9);
                        
desc vacunatorios;
desc vacunas;