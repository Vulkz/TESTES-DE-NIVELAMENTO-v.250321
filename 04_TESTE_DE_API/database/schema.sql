CREATE DATABASE IF NOT EXISTS teste_de_banco_de_dados;
USE teste_de_banco_de_dados;

CREATE TABLE operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans VARCHAR(20) UNIQUE,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    modalidade VARCHAR(100),
    uf VARCHAR(2),
    data_registro DATE
);
