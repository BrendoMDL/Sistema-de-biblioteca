
import os

# Define um banco SQLite temporário antes de importar a aplicação.
# Isso evita que os testes dependam do banco de desenvolvimento.
os.environ["DATABASE_URL"] = "sqlite://"

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

# Cria um banco SQLite em memória, compartilhado pelos testes.
engine_teste = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

SessaoTeste = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_teste,
)

# Cria as tabelas no banco temporário.
Base.metadata.create_all(bind=engine_teste)


# Substitui a conexão normal pela conexão de teste.
def obter_banco_teste():
    banco = SessaoTeste()
    try:
        yield banco
    finally:
        banco.close()


app.dependency_overrides[get_db] = obter_banco_teste
cliente = TestClient(app)


# Teste 1: a rota principal deve responder com sucesso.
def test_rota_inicial():
    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert resposta.json()["mensagem"] == (
        "API da Biblioteca funcionando!"
    )


# Teste 2: a rota de listagem deve retornar uma lista vazia
# quando não houver livros cadastrados.
def test_listar_livros_vazio():
    Base.metadata.drop_all(bind=engine_teste)
    Base.metadata.create_all(bind=engine_teste)

    resposta = cliente.get("/livros/")

    assert resposta.status_code == 200
    assert resposta.json() == []


# Teste 3: cadastrar um livro deve retornar HTTP 201.
def test_criar_livro():
    Base.metadata.drop_all(bind=engine_teste)
    Base.metadata.create_all(bind=engine_teste)

    livro = {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "isbn": "9780000000001",
        "editora": "Editora Teste",
        "ano_publicacao": 1899,
        "categoria": "Romance",
        "quantidade": 3,
        "descricao": "Livro utilizado no teste automatizado",
    }

    resposta = cliente.post("/livros/", json=livro)

    assert resposta.status_code == 201
    assert resposta.json()["titulo"] == "Dom Casmurro"
    assert resposta.json()["quantidade"] == 3
