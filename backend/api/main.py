from io import BytesIO
from typing import List
from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import StreamingResponse
import fitz
from .services.pdf_convert_service import pdf_convert_to_text

import os
import pytesseract
import numpy as np
import cv2 # OpenCV
from PIL import Image
# from google.colab.patches import cv2_imshow # para mostrar as imagens no Google Colab


app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Bem-vindo ao API OCR pdf to txt"}

@app.post("/join_pdf")
async def join_pdf(pdf_files: List[UploadFile], output_file_name:str = Form("out.pdf")):
    new_pdf = fitz.open()
    for pdf_file in pdf_files:
        pdf_stream = await pdf_file.read()
        try:
            pdf = fitz.open(None, pdf_stream, "pdf")
        except:
            raise HTTPException(status_code=400, detail=f"O arquivo {pdf_file.filename} não é um PDF válido.")
        new_pdf.insert_pdf(pdf)
    
    new_pdf_buffer = BytesIO(new_pdf.tobytes())

    headers = {
        'Content-Disposition': f'attachment; filename={output_file_name}'
    }

    return StreamingResponse(new_pdf_buffer, headers=headers, media_type="application/pdf")


# @app.post("/pdf_to_txt")
# async def pdf_to_txt(pdf_file: UploadFile):
    pdf_stream = await pdf_file.read()
    try:
        pdf = fitz.open(None, pdf_stream, "pdf")
    except:
        raise HTTPException(status_code=400, detail=f"O arquivo: {pdf_file.filename}, não é um PDF válido.")
    

    #teste

    # Chama a função pdf_to_txt para converter o PDF em texto
    text = pdf_to_txt(pdf_stream)

    #te4ste

    # text = ""
    # for page in pdf:
    #     text += page.get_text()
    
    return {"text": text}


# teste img_to_txt

@app.post("/img_to_txt")
async def img_to_txt(img_file: UploadFile):
    try:
        # # Lê os bytes do arquivo de imagem
        # img_bytes = await img_file.read()
        
        # # Converte os bytes em uma matriz numpy
        # nparr = np.frombuffer(img_bytes, np.uint8)
        
        # # Decodifica a matriz numpy em uma imagem OpenCV
        # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # # Usa pytesseract para extrair texto da imagem
        # text = pytesseract.image_to_string(img)

        # Lê o arquivo de imagem
        # img = cv2.imread(img_file.file)
        # img = Image.open(BytesIO(img_bytes))
        
        # config_tesseract = '--tessdata-dir tessdata' # Caminho para o diretório de dados de treinamento do Tesseract
        config_tesseract = f'--tessdata-dir {os.environ["TESSDATA_PREFIX"]}'


        # Abre a imagem usando PIL
        img = Image.open(img_file.file)
        
        # Converte a imagem para um array numpy
        img_array = np.array(img)
        
        # Converte a imagem para escala de cinza
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        
        # Usa pytesseract para extrair texto da imagem na limguagem portuguesa
        # text = pytesseract.image_to_string(gray, lang='por', config=config_tesseract)

        text = pytesseract.image_to_string(gray, lang='por', config=config_tesseract)
        
        return {"text": text}
    except Exception as e:
        # Se ocorrer algum erro, retorne uma mensagem de erro adequada
        return {"error": f"Ocorreu um erro ao processar a imagem: {str(e)}"}
