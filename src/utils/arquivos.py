import os
import requests
from zipfile import ZipFile

def baixar_pdf(link, destino):
    nome_arquivo = os.path.basename(link)
    caminho = os.path.join(destino, nome_arquivo)

    if os.path.exists(caminho):
        print(f"{nome_arquivo} já existe")
        return caminho

    print(f"Baixando {nome_arquivo}...")
    resposta = requests.get(link)
    with open(caminho, "wb") as f:
        f.write(resposta.content)

    return caminho

def compactar_em_zip(lista_de_arquivos, nome_arquivo_zip):
    print(f"Compactando arquivos em {nome_arquivo_zip}...")
    os.makedirs(os.path.dirname(nome_arquivo_zip), exist_ok=True)

    with ZipFile(nome_arquivo_zip, 'w') as zipf:
        for arquivo in lista_de_arquivos:
            zipf.write(arquivo, arcname=os.path.basename(arquivo))

    print("Compactação finalizada com sucesso!")
