import pytesseract
import numpy as np
import cv2 
# from google.colab.patches import cv2_imshow


def pdf_convert_to_text(pdf_file):
    # Converte o PDF em uma lista de imagens
    pages = convert_from_path(pdf_file, 300)

    # Inicializa uma   string para armazenar o texto extraído de todas as páginas
    full_text = ""

    # Loop pelas páginas e extrai o texto de cada uma
    for page in pages:
        # Converte a imagem para escala de cinza
        gray = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2GRAY)
        
        # Usa pytesseract para extrair texto da imagem
        text = pytesseract.image_to_string(gray)
        
        # Adiciona o texto extraído à string completa
        full_text += text + "\n"

    return full_text



# ///chat

# import pytesseract
# from pdf2image import convert_from_path
# import os

# def pdf_to_text(pdf_file_path, output_text_file):
#     # Converte o PDF em uma lista de imagens
#     pages = convert_from_path(pdf_file_path, 300)

#     # Inicializa uma string para armazenar o texto extraído de todas as páginas
#     full_text = ""

#     # Loop pelas páginas e extrai o texto de cada uma
#     for page in pages:
#         # Converte a imagem para escala de cinza
#         gray = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2GRAY)
        
#         # Usa pytesseract para extrair texto da imagem
#         text = pytesseract.image_to_string(gray)
        
#         # Adiciona o texto extraído à string completa
#         full_text += text + "\n"

#     # Salva o texto extraído em um arquivo .txt
#     with open(output_text_file, 'w') as f:
#         f.write(full_text)

#     print("Texto extraído e salvo com sucesso em", output_text_file)

# # Exemplo de uso da função
# pdf_file_path = "seu_arquivo.pdf"
# output_text_file = "texto_extraido.txt"
# pdf_to_text(pdf_file_path, output_text_file)
