# Api de OCR (PDF TO TXT)

API desenvolvida em Python, contém a finalidade de extrair texto de aquivo como imagem e pdf.

A Api conta com os endpoints:

`POST /img_to_string` Para envio de um arquivo de imagem e retorna um body com a string extraída.

`POST /pdf_to_txt` Para envio de um arquivo tipo pdf e retorna um zip contendo um arquivo .txt para cada pagina do pdf que foi extraída.

# 🛠 Requisitos para iniciar a aplicação

## Ferramentas

- **VsCode**
- **Docker compose**

---

## 🛠 Tecnologias

As seguintes tecnologias foram utilizadas no desenvolvimento da API do projeto:

- **[FastAPI](https://fastapi.tiangolo.com/)**
- **[Python](https://pypi.org/)**
- **[Pytesseract](https://pypi.org/project/pytesseract/)**
- **[OpenCV](https://opencv.org/)**
- **[Pillow](https://pypi.org/project/pillow/)**
- **[Docker](https://www.docker.com/)**

---

## Passos para iniciar a aplicação

Na raiz do projeto com o terminal aberto rodo os comandos para iniciar

- `docker compose build`
- `docker compose up` ou `docker compose up -d`

### Pronto para testar

- Abra o seu navegador e acesse `http://localhost:8000/docs`

- Para efetuar um teste foi usado um pdf do edital de concurso do "ibfc"
  **[Disponível aqui](https://anexos.cdn.selecao.net.br/uploads/747/concursos/460/anexos/VB1NI1TFmqsFswK4RLtra42834T46Gb6D69TeHXa.pdf)**

- Vídeo do teste realizado **[Disponível aqui](https://youtu.be/67c0qTDsBwk)**
