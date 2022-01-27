CREATE DATABASE lucasf1_bdd_1st;

USE lucasf1_bdd_1st;

CREATE TABLE pessoas(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    nascimento VARCHAR(255) NOT NULL
);
