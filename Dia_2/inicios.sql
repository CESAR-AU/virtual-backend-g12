create database prueba;
use prueba;

create table clientes(
    id int auto_increment primary key,
    nombre char(100) UNIQUE,
    documento varchar(10) UNIQUE,
    tipo_documento enum('C.E', 'DNI','RUC', 'PASAPORTE'),
    estado bool
);