from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(100), nullable=False)

    cpf = Column(String(14), unique=True, nullable=False, index=True)

    email = Column(String(150), unique=True, nullable=False, index=True)

    telefone = Column(String(20), nullable=True)

    senha = Column(String(255), nullable=False)

    tipo = Column(String(20), nullable=False, default="usuario")

    emprestimos = relationship(
        "Emprestimo",
        back_populates="usuario"
    )