# # Use a imagem oficial do Python como base
FROM python:3.9

#teste
# Instalar dependências
RUN apt-get update && \
    apt-get install -y tesseract-ocr-por libgl1-mesa-glx

# Instalar pacotes Python
RUN pip install opencv-python pytesseract

# Definir a variável de ambiente TESSDATA_PREFIX
# ENV TESSDATA_PREFIX=/backend/api/tessdata
ENV TESSDATA_PREFIX=/code/api/tessdata

#teste


# Define o diretório de trabalho dentro do contêiner
WORKDIR /code

# Copie os arquivos necessários para o diretório de trabalho no contêiner
COPY ./requirements.txt /code/requirements.txt

# Instale as dependências do aplicativo
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copie os arquivos necessários para o diretório de trabalho no contêiner
COPY ./api /code/api

# Comando para executar o aplicativo quando o contêiner for iniciado
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]