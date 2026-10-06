from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.models.livro import Livro
from app.models.emprestimo import Emprestimo
from app.schemas.emprestimo import (
    EmprestimoCreate,
    EmprestimoResponse
)


router = APIRouter(
    prefix="/emprestimos",
    tags=["Empréstimos"]
)


@router.post(
    "/",
    response_model=EmprestimoResponse,
    status_code=201
)
def criar_emprestimo(
    dados: EmprestimoCreate,
    db: Session = Depends(get_db)
):

    # Verifica se o usuário existe
    usuario = (
        db.query(Usuario)
        .filter(Usuario.id == dados.usuario_id)
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )

    # Verifica se o livro existe
    livro = (
        db.query(Livro)
        .filter(Livro.id == dados.livro_id)
        .first()
    )

    if not livro:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado."
        )

    # Verifica se existe livro disponível
    if livro.quantidade <= 0:
        raise HTTPException(
            status_code=400,
            detail="Não existem exemplares disponíveis."
        )

    # Cria o empréstimo
    novo_emprestimo = Emprestimo(
        usuario_id=dados.usuario_id,
        livro_id=dados.livro_id,
        data_prevista_devolucao=(
            dados.data_prevista_devolucao
        ),
        status="emprestado"
    )

    # Diminui a quantidade disponível
    livro.quantidade -= 1

    db.add(novo_emprestimo)
    db.commit()
    db.refresh(novo_emprestimo)

    return novo_emprestimo


@router.get(
    "/",
    response_model=list[EmprestimoResponse]
)
def listar_emprestimos(
    db: Session = Depends(get_db)
):
    emprestimos = (
        db.query(Emprestimo)
        .all()
    )

    return emprestimos


@router.get(
    "/{emprestimo_id}",
    response_model=EmprestimoResponse
)
def buscar_emprestimo(
    emprestimo_id: int,
    db: Session = Depends(get_db)
):
    emprestimo = (
        db.query(Emprestimo)
        .filter(Emprestimo.id == emprestimo_id)
        .first()
    )

    if not emprestimo:
        raise HTTPException(
            status_code=404,
            detail="Empréstimo não encontrado."
        )

    return emprestimo


@router.put(
    "/{emprestimo_id}/devolver",
    response_model=EmprestimoResponse
)
def devolver_livro(
    emprestimo_id: int,
    db: Session = Depends(get_db)
):
    emprestimo = (
        db.query(Emprestimo)
        .filter(Emprestimo.id == emprestimo_id)
        .first()
    )

    if not emprestimo:
        raise HTTPException(
            status_code=404,
            detail="Empréstimo não encontrado."
        )

    if emprestimo.status == "devolvido":
        raise HTTPException(
            status_code=400,
            detail="Este livro já foi devolvido."
        )

    livro = (
        db.query(Livro)
        .filter(Livro.id == emprestimo.livro_id)
        .first()
    )

    if not livro:
        raise HTTPException(
            status_code=404,
            detail="Livro relacionado ao empréstimo não encontrado."
        )

    from datetime import date

    emprestimo.data_devolucao = date.today()
    emprestimo.status = "devolvido"

    livro.quantidade += 1

    db.commit()
    db.refresh(emprestimo)

    return emprestimo