USE ans_dados;


LOAD DATA LOCAL INFILE 'C:/Users/enzov/Downloads/1T2023.csv'
INTO TABLE demonstrativos
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ano, trimestre, registro_ans, razao_social, conta_contabil, descricao_conta, valor);

LOAD DATA LOCAL INFILE 'C:/Users/enzov/Downloads/2T2023.csv'
INTO TABLE demonstrativos
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ano, trimestre, registro_ans, razao_social, conta_contabil, descricao_conta, valor);

LOAD DATA LOCAL INFILE 'C:/Users/enzov/Downloads/3T2023.csv'
INTO TABLE demonstrativos
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ano, trimestre, registro_ans, razao_social, conta_contabil, descricao_conta, valor);

LOAD DATA LOCAL INFILE 'C:/Users/enzov/Downloads/4T2023.csv'
INTO TABLE demonstrativos
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ano, trimestre, registro_ans, razao_social, conta_contabil, descricao_conta, valor);

LOAD DATA LOCAL INFILE 'C:/Users/enzov/Downloads/1T2024.csv'
INTO TABLE demonstrativos
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ano, trimestre, registro_ans, razao_social, conta_contabil, descricao_conta, valor);

LOAD DATA LOCAL INFILE 'C:/Users/enzov/Downloads/2T2024.csv'
INTO TABLE demonstrativos
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ano, trimestre, registro_ans, razao_social, conta_contabil, descricao_conta, valor);

LOAD DATA LOCAL INFILE 'C:/Users/enzov/Downloads/3T2024.csv'
INTO TABLE demonstrativos
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ano, trimestre, registro_ans, razao_social, conta_contabil, descricao_conta, valor);

LOAD DATA LOCAL INFILE 'C:/Users/enzov/Downloads/4T2024.csv'
INTO TABLE demonstrativos
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ano, trimestre, registro_ans, razao_social, conta_contabil, descricao_conta, valor);


LOAD DATA LOCAL INFILE 'C:/Users/enzov/Downloads/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';' ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(registro_ans, cnpj, razao_social, modalidade, uf, municipio, data_registro);
