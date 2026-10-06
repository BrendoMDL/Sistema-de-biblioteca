from fastapi import FastAPI

# Cria a aplicação FastAPI
app = FastAPI(
    title="Sistema de Biblioteca",
    description="API para gerenciamento de uma biblioteca",
    version="1.0.0"
)


@app.get("/")
def raiz():
    return {
        "mensagem": "API da Biblioteca funcionando!"
    }