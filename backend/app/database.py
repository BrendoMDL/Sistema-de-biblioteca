
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Carrega as variáveis do arquivo .env durante o desenvolvimento.
# No Render, as variáveis são fornecidas pelo próprio ambiente.
load_dotenv()

# Obtém o endereço de conexão com o PostgreSQL.
DATABASE_URL = os.getenv("DATABASE_URL")

# Verifica se a variável foi configurada.
if not DATABASE_URL:
    raise RuntimeError("A variável DATABASE_URL não foi configurada.")

# Ajusta a URL para utilizar o driver Psycopg 3.
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql+psycopg://",
        1
    )
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )

# Cria a conexão com o banco PostgreSQL.
engine = create_engine(DATABASE_URL)

# Configura as sessões utilizadas pelas operações do banco.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para os modelos do SQLAlchemy.
Base = declarative_base()


# Fornece uma sessão do banco para as rotas da API.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
