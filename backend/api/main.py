from fastapi.responses import StreamingResponse
from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import StreamingResponse
from .services.pdf_convert_service import img_convert_to_string
from .services.pdf_convert_service import pdf_convert_to_text

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Bem-vindo ao API OCR pdf to txt"}

@app.post("/img_to_string")
async def img_to_string(img_file: UploadFile):
    try:
        text = img_convert_to_string(img_file)

        return {"text": text}
    except Exception as e:
        # Se ocorrer algum erro, retorne uma mensagem de erro adequada
        return {"error": f"Ocorreu um erro ao processar a imagem: {str(e)}"}

@app.post("/pdf_to_txt")
async def pdf_to_txt(pdf_file: UploadFile):
    try:
        # Chama pdf_convert_to_text para processar o PDF e obter o texto de cada página e o nome do arquivo zip
        zip_filename = await pdf_convert_to_text(pdf_file)

        # Retorna o arquivo zip para download
        return StreamingResponse(
            open(zip_filename, "rb"),
            media_type="application/zip",
            headers={"Content-Disposition": f"attachment; filename={zip_filename}"}
        )
    except Exception as e:
        # Se ocorrer algum erro, retorne uma mensagem de erro adequada
        return {"error": f"Ocorreu um erro : {str(e)}"}