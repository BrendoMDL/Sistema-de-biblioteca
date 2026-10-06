from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.livro import Livro
from app.schemas.livro import (
    LivroCreate,
    LivroResponse,
    LivroUpdate
)


router = APIRouter(
    prefix="/livros",
    tags=["Livros"]
)


@router.post(
    "/",
    response_model=LivroResponse,
    status_code=201
)
def criar_livro(
    livro: LivroCreate,
    db: Session = Depends(get_db)
):
    livro_existente = (
        db.query(Livro)
        .filter(Livro.isbn == livro.isbn)
        .first()
    )

    if livro_existente:
        raise HTTPException(
            status_code=400,
            detail="Já existe um livro cadastrado com este ISBN."
        )

    novo_livro = Livro(
        titulo=livro.titulo,
        autor=livro.autor,
        isbn=livro.isbn,
        editora=livro.editora,
        ano_publicacao=livro.ano_publicacao,
        categoria=livro.categoria,
        quantidade=livro.quantidade,
        descricao=livro.descricao
    )

    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)

    return novo_livro


@router.get(
    "/",
    response_model=list[LivroResponse]
)
def listar_livros(
    db: Session = Depends(get_db)
):
    livros = db.query(Livro).all()

    return livros


@router.get(
    "/{livro_id}",
    response_model=LivroResponse
)
def buscar_livro(
    livro_id: int,
    db: Session = Depends(get_db)
):
    livro = (
        db.query(Livro)
        .filter(Livro.id == livro_id)
        .first()
    )

    if not livro:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado."
        )

    return livro


@router.put(
    "/{livro_id}",
    response_model=LivroResponse
)
def atualizar_livro(
    livro_id: int,
    dados: LivroUpdate,
    db: Session = Depends(get_db)
):
    livro = (
        db.query(Livro)
        .filter(Livro.id == livro_id)
        .first()
    )

    if not livro:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado."
        )

    dados_atualizacao = dados.model_dump(
        exclude_unset=True
    )

    for campo, valor in dados_atualizacao.items():
        setattr(livro, campo, valor)

    db.commit()
    db.refresh(livro)

    return livro


@router.delete(
    "/{livro_id}"
)
def excluir_livro(
    livro_id: int,
    db: Session = Depends(get_db)
):
    livro = (
        db.query(Livro)
        .filter(Livro.id == livro_id)
        .first()
    )

    if not livro:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado."
        )

    if livro.emprestimos:
        raise HTTPException(
            status_code=400,
            detail=(
                "Não é possível excluir este livro "
                "porque existem empréstimos relacionados."
            )
        )

    db.delete(livro)
    db.commit()

    return {
        "mensagem": "Livro excluído com sucesso."
    }