from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.models.usuario import Usuario
from app.models.livro import Livro
from app.models.emprestimo import Emprestimo

from app.routers import livros
from app.routers import usuarios
from app.routers import emprestimos


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Sistema de Biblioteca",
    description="API para gerenciamento de uma biblioteca",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    livros.router
)

app.include_router(
    usuarios.router
)

app.include_router(
    emprestimos.router
)


@app.get("/")
def raiz():
    return {
        "mensagem": "API da Biblioteca funcionando!"
    }