from datetime import date

from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    livro_id = Column(
        Integer,
        ForeignKey("livros.id"),
        nullable=False
    )

    data_emprestimo = Column(
        Date,
        nullable=False,
        default=date.today
    )

    data_prevista_devolucao = Column(
        Date,
        nullable=False
    )

    data_devolucao = Column(
        Date,
        nullable=True
    )

    status = Column(
        String(20),
        nullable=False,
        default="emprestado"
    )

    usuario = relationship(
        "Usuario",
        back_populates="emprestimos"
    )

    livro = relationship(
        "Livro",
        back_populates="emprestimos"
    )