CREATE DATABASE colegio;
USE colegio;
CREATE TABLE IF NOT EXISTS tbl_alumnos(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(100) NOT NULL,
    apellido_paterno VARCHAR(100),
    apellido_materno VARCHAR(100),
    correo VARCHAR(50) UNIQUE,
    numero_emergencia VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS tbl_nivel(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(100) NOT NULL,
    apellido_paterno VARCHAR(100),
    apellido_materno VARCHAR(100),
    correo VARCHAR(50) UNIQUE,
    numero_emergencia VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS tbl_alumnos_niveles(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    fecha_cursada YEAR NOT NULL,
    alumnos_id INT,
    nivel_id INT,
    FOREIGN KEY (alumnos_id) REFERENCES tbl_alumnos(id),
    FOREIGN KEY (nivel_id) REFERENCES tbl_nivel(id)
);