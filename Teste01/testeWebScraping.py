import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

URL_SITE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
DESTINO_PASTA = "pdfs_baixados"
NOME_ZIP = "AnexosI_II.zip"

def buscar_links_dos_pdfs(url):
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.content, "html.parser")
    links_pdf = []

    for link in soup.find_all('a', href=True):
        href = link['href']
        if "Anexo_I" in href or "Anexo_II" in href:
            if href.endswith(".pdf"):
                if not href.startswith("http"):
                    href = "https://www.gov.br" + href
                links_pdf.append(href)
    
    return links_pdf

def baixar_pdf(link, destino):
    nome_arquivo = os.path.basename(link)
    caminho = os.path.join(destino, nome_arquivo)
    print(f"Baixando {nome_arquivo}...")
    resposta = requests.get(link)
    with open(caminho, "wb") as f:
        f.write(resposta.content)
    return caminho

def compactar_em_zip(lista_de_arquivos, nome_arquivo_zip):
    print("Compactando arquivos...")
    with ZipFile(nome_arquivo_zip, 'w') as zipf:
        for arquivo in lista_de_arquivos:
            zipf.write(arquivo, arcname=os.path.basename(arquivo))
    print("Compactação finalizada com sucesso!")

def main():
    os.makedirs(DESTINO_PASTA, exist_ok=True)

    links = buscar_links_dos_pdfs(URL_SITE)
    arquivos_baixados = [baixar_pdf(link, DESTINO_PASTA) for link in links]
    compactar_em_zip(arquivos_baixados, NOME_ZIP)

if __name__ == "__main__":
    main()
