import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.emprestimo import Emprestimo  # noqa: F401
from app.models.livro import Livro  # noqa: F401
from app.models.usuario import Usuario  # noqa: F401
from app.routers import emprestimos, livros, usuarios

# Cria as tabelas do banco de dados, caso ainda não existam.
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Sistema de Biblioteca",
    description="API para gerenciamento de uma biblioteca",
    version="1.0.0"
)


# Obtém as origens autorizadas a acessar a API.
# No Render, FRONTEND_URL será configurada posteriormente.
# Localmente, mantém o endereço padrão do Vite.
origens_permitidas = os.getenv(
    "FRONTEND_URL",
    "http://localhost:5173"
).split(",")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        origem.strip()
        for origem in origens_permitidas
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Registra as rotas da aplicação.
app.include_router(livros.router)
app.include_router(usuarios.router)
app.include_router(emprestimos.router)


@app.get("/")
def raiz():
    return {
        "mensagem": "API da Biblioteca funcionando!"
    }
