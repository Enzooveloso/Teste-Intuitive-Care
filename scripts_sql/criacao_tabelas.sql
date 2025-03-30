CREATE DATABASE IF NOT EXISTS ans_dados;
USE ans_dados;


CREATE TABLE IF NOT EXISTS demonstrativos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ano INT,
  trimestre VARCHAR(10),
  registro_ans VARCHAR(20),
  razao_social VARCHAR(255),
  conta_contabil VARCHAR(255),
  descricao_conta VARCHAR(255),
  valor DECIMAL(18, 2)
);


CREATE TABLE IF NOT EXISTS operadoras (
  id INT AUTO_INCREMENT PRIMARY KEY,
  registro_ans VARCHAR(20),
  cnpj VARCHAR(20),
  razao_social VARCHAR(255),
  modalidade VARCHAR(100),
  uf VARCHAR(5),
  municipio VARCHAR(100),
  data_registro DATE
);
