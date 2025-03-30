import pdfplumber
import pandas as pd
import os
from zipfile import ZipFile

CAMINHO_PDF = "data/pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
NOME_CSV = "data/rol_procedimentos.csv"
NOME_ZIP = "output/Teste_enzo.zip"


SUBSTITUIR_COLUNAS = {
    "OD": "Odontologia",
    "AMB": "Ambulatorial"
}

def extrair_tabela_pdf(caminho_pdf):
    print("Extraindo tabelas do PDF...")
    tabelas = []

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            tabela = pagina.extract_table()
            if tabela:
                df = pd.DataFrame(tabela[1:], columns=tabela[0])
                tabelas.append(df)

    if not tabelas:
        raise ValueError("Nenhuma tabela foi encontrada no PDF.")

    df_final = pd.concat(tabelas, ignore_index=True)
    print(f"{len(df_final)} linhas extraídas.")
    return df_final

def substituir_abreviacoes(df):
    print("Substituindo abreviações nas colunas...")
    for col in df.columns:
        if col in SUBSTITUIR_COLUNAS:
            df[col] = df[col].replace(SUBSTITUIR_COLUNAS)
    return df

def salvar_zipar_csv(df, nome_csv, nome_zip):
    print("Salvando CSV e compactando...")
    os.makedirs(os.path.dirname(nome_csv), exist_ok=True)
    os.makedirs(os.path.dirname(nome_zip), exist_ok=True)

    df.to_csv(nome_csv, index=False)

    with ZipFile(nome_zip, 'w') as zipf:
        zipf.write(nome_csv, arcname=os.path.basename(nome_csv))

    print(f"Arquivo CSV salvo e compactado em: {nome_zip}")

def main():
    df = extrair_tabela_pdf(CAMINHO_PDF)
    df = substituir_abreviacoes(df)
    salvar_zipar_csv(df, NOME_CSV, NOME_ZIP)

if __name__ == "__main__":
    main()
