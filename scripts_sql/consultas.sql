USE ans_dados;
-- Top 10 operadoras com maiores despesas no último trimestre (4T2024)
SELECT
    demo.registro_ans, op.razao_social, SUM(d.valor) AS total_despesa
FROM demonstrativos demo
JOIN operadoras op ON demo.registro_ans = op.registro_ans
WHERE demo.conta_contabil LIKE '%SINISTROS CONHECIDOS%'
  AND demo.descricao_conta LIKE '%ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR%'
  AND demo.ano = 2024
  AND demo.trimestre = '4T'
GROUP BY demo.registro_ans, op.razao_social
ORDER BY total_despesa DESC
LIMIT 10;

-- Top 10 operadoras com maiores despesas no último ano completo (2024)
SELECT
    demo.registro_ans, op.razao_social, SUM(demo.valor) AS total_despesa
FROM demonstrativos demo
JOIN operadoras op ON demo.registro_ans = op.registro_ans
WHERE demo.conta_contabil LIKE '%SINISTROS CONHECIDOS%'
  AND demo.descricao_conta LIKE '%ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR%'
  AND demo.ano = 2024
GROUP BY demo.registro_ans, op.razao_social
ORDER BY total_despesa DESC
LIMIT 10;