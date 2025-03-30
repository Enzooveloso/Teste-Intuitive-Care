import os
import zipfile

PASTA_ZIPS = "data/contabeis"

def descompactar_zips(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".zip"):
            caminho_zip = os.path.join(pasta, arquivo)
            print(f"Descompactando: {arquivo}")
            try:
                with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                    zip_ref.extractall(pasta)
                print(f"{arquivo} descompactado!\n")
            except zipfile.BadZipFile:
                print(f"Erro: {arquivo} não é um arquivo ZIP válido.")

def remover_zips(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".zip"):
            caminho = os.path.join(pasta, arquivo)
            os.remove(caminho)
            print(f"Removido: {arquivo}")

if __name__ == "__main__":
    descompactar_zips(PASTA_ZIPS)
    remover_zips(PASTA_ZIPS)
