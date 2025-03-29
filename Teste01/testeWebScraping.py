import zipfile
import os

def compactar_para_zip(lista_de_arquivos, nome_do_zip="Anexo_I_&_II.zip"):
    with zipfile.ZipFile(nome_do_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for caminho in lista_de_arquivos:
            if os.path.isfile(caminho):
                nome_arquivo = os.path.basename(caminho)
                zipf.write(caminho, arcname=nome_arquivo)
            else:
                print(f"Arquivo nao encontrado: {caminho}")
    print(f"Arquivos compactados em: {nome_do_zip}")


Pdfs = ["Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"]
compactar_para_zip(Pdfs)
