# # Use a imagem oficial do Python como base
# FROM python:3.9

# # Define o diretório de trabalho dentro do contêiner
# WORKDIR /app

# # Copie os arquivos necessários para o diretório de trabalho no contêiner
# COPY . .

# # Instale as dependências do aplicativo
# RUN pip install --no-cache-dir -r requirements.txt

# # RUN pip install -r requirements.txt
# # RUN pip install -r requirements-dev.txt

# # Comando para executar o aplicativo quando o contêiner for iniciado
# CMD ["python", "-m", "api.main:app"]

# nova versão fastapi docs
# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./api /code/api

# 
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]