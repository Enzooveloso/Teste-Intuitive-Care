from bs4 import BeautifulSoup
import requests
import os

from utils.arquivos import baixar_pdf, compactar_em_zip
from config import PDF_DIR, ZIP_PDFS

URL_SITE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def buscar_links_dos_pdfs(url):
    print("Buscando links dos PDFs na página da ANS...")
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

    print(f"Encontrados {len(links_pdf)} links de PDF.")
    return links_pdf

def main():
    os.makedirs(PDF_DIR, exist_ok=True)

    links = buscar_links_dos_pdfs(URL_SITE)
    arquivos_baixados = [baixar_pdf(link, PDF_DIR) for link in links]
    compactar_em_zip(arquivos_baixados, ZIP_PDFS)

if __name__ == "__main__":
    main()
