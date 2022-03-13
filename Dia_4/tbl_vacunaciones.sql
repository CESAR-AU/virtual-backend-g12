CREATE TABLE vacunaciones(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) UNIQUE NOT NULL,
    estado BOOL DEFAULT true,
    fecha_vencimiento DATE,
    procedencia ENUM('USA', 'CHINA', 'RUSIA', 'UK'),
    lote VARCHAR(10)    
)
