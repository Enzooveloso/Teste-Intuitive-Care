import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import pandas as pd
from sqlalchemy.orm import Session
from src.db.database import SessionLocal
from src.db import models

ARQUIVO_CSV = "data/operadoras/Relatorio_cadop.csv"

def importar_operadoras():
    df = pd.read_csv(ARQUIVO_CSV, sep=";", encoding="latin1", dtype=str)
    df = df.fillna("")

    session: Session = SessionLocal()
    adicionados = 0

    for _, row in df.iterrows():
        try:
            operadora = models.Operadora(
                registro_ans=int(row["Registro_ANS"]),
                cnpj=row["CNPJ"],
                razao_social=row["Razao_Social"],
                modalidade=row["Modalidade"],
                uf=row["UF"],
                municipio=row["Cidade"],
                data_registro=row["Data_Registro_ANS"]
            )
            session.merge(operadora)  # insere ou atualiza
            adicionados += 1
        except Exception as e:
            print(f"Erro ao processar linha: {e}")
    session.commit()
    session.close()

    print(f"Importação concluída: {adicionados} operadoras adicionadas.")

if __name__ == "__main__":
    importar_operadoras()
