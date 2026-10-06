from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import (
    UsuarioCreate,
    UsuarioResponse
)


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


@router.post(
    "/",
    response_model=UsuarioResponse,
    status_code=201
)
def criar_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario_email = (
        db.query(Usuario)
        .filter(Usuario.email == usuario.email)
        .first()
    )

    if usuario_email:
        raise HTTPException(
            status_code=400,
            detail="Já existe um usuário com este e-mail."
        )

    usuario_cpf = (
        db.query(Usuario)
        .filter(Usuario.cpf == usuario.cpf)
        .first()
    )

    if usuario_cpf:
        raise HTTPException(
            status_code=400,
            detail="Já existe um usuário com este CPF."
        )

    novo_usuario = Usuario(
        nome=usuario.nome,
        cpf=usuario.cpf,
        email=usuario.email,
        telefone=usuario.telefone,
        senha=usuario.senha,
        tipo=usuario.tipo
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


@router.get(
    "/",
    response_model=list[UsuarioResponse]
)
def listar_usuarios(
    db: Session = Depends(get_db)
):
    usuarios = db.query(Usuario).all()

    return usuarios


@router.get(
    "/{usuario_id}",
    response_model=UsuarioResponse
)
def buscar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = (
        db.query(Usuario)
        .filter(Usuario.id == usuario_id)
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )

    return usuario