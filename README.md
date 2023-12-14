# trabalhocoding

MYSQL

CREATE DATABASE clinica_odontologica;
USE clinica_odontologica;

CREATE TABLE pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    email VARCHAR(100),
    telefone VARCHAR(20)
);
