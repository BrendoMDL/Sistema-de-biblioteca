
FROM python:3.12-slim

# Define a pasta de trabalho dentro do container.
WORKDIR /app

# Instala as dependências da API.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do backend.
COPY app ./app

# Expõe a porta padrão do Render.
EXPOSE 10000

# Inicia o servidor FastAPI utilizando a porta fornecida pelo Render.
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}"]
