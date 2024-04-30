import pytesseract # Pytesseract
import numpy as np # NumPy
import cv2 # OpenCV
import os # Módulo os
import fitz  # PyMuPDF
import zipfile  # Importa o módulo zipfile

# Importa o módulo Image do pacote PIL
from PIL import Image

def img_convert_to_string(img_file):
    text = ""
    try:
        # config_tesseract = '--tessdata-dir tessdata' # Caminho para o diretório de dados de treinamento do Tesseract
        config_tesseract = f'--tessdata-dir {os.environ["TESSDATA_PREFIX"]}'
        # Abre a imagem usando PIL
        img = Image.open(img_file.file)
        # Converte a imagem para um array numpy
        img_array = np.array(img)
        # Converte a imagem para escala de cinza
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        # Usa pytesseract para extrair texto da imagem na limguagem portuguesa
        text = pytesseract.image_to_string(gray, lang='por', config=config_tesseract)
        
        return text
    except Exception as e:
        raise Exception(f"Erro ao converter: {str(e)}")


async def pdf_convert_to_text(pdf_file):
    # config_tesseract = '--tessdata-dir tessdata' # Caminho para o diretório de dados de treinamento do Tesseract
    config_tesseract = f'--tessdata-dir {os.environ["TESSDATA_PREFIX"]}'
    # Lê o arquivo PDF
    pdf_stream = await pdf_file.read()
    try:
        # Abre o arquivo PDF
        doc = fitz.open(None, pdf_stream, "pdf")

        # Inicializa a lista de textos
        texts = []
        # Itera sobre cada página do PDF
        for i, page in enumerate(doc):
            # Renderiza a página como uma imagem
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            # Converte a imagem para um array numpy
            img_array = np.array(img)
            # Converte a imagem para escala de cinza
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            # Usa pytesseract para extrair texto da imagem na limguagem portuguesa
            text = pytesseract.image_to_string(gray, lang='por', config=config_tesseract)

            # Adiciona o texto da página à lista de textos
            texts.append([text])

            # Cria um diretório para salvar os arquivos de texto, se não existir
            directory = "textos"
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Cria um arquivo .txt para a página atual
            filename = os.path.join(directory, f"page_{i+1}.txt")  # Caminho completo do arquivo
            with open(filename, "w") as f:
                f.write(text)

        # Fecha o documento PDF
        doc.close()

        # Cria um arquivo zip contendo todos os arquivos de texto
        zip_filename = "textos.zip"
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            for root, _, files in os.walk(directory):
                for file in files:
                    zipf.write(os.path.join(root, file), file)

        # Exclui os arquivos .txt após a criação do arquivo zip
        for root, _, files in os.walk(directory):
            for file in files:
                os.remove(os.path.join(root, file))

        return zip_filename
    except Exception as e:
        raise Exception(f"Erro ao converter: {str(e)}")