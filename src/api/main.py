from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import csv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_PATH = os.path.join("data", "operadoras", "Relatorio_cadop.csv")

@app.get("/operadoras")
def buscar_operadoras(q: str = Query(..., min_length=1)) -> List[dict]:
    resultados = []
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            if q.lower() in row['Razao_Social'].lower():
                resultados.append({
                    "registro_ans": row['Registro_ANS'],
                    "razao_social": row['Razao_Social'],
                    "cnpj": row['CNPJ'],
                    "modalidade": row['Modalidade'],
                    "uf": row['UF'],
                    "municipio": row['Cidade'],
                    "data_registro": row['Data_Registro_ANS'],      
                })
    return resultados
