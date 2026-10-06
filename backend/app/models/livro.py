from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)

    titulo = Column(String(200), nullable=False, index=True)

    autor = Column(String(150), nullable=False, index=True)

    isbn = Column(String(20), unique=True, nullable=False, index=True)

    editora = Column(String(150), nullable=True)

    ano_publicacao = Column(Integer, nullable=True)

    categoria = Column(String(100), nullable=True, index=True)

    quantidade = Column(Integer, nullable=False, default=0)

    descricao = Column(Text, nullable=True)

    emprestimos = relationship(
        "Emprestimo",
        back_populates="livro"
    )