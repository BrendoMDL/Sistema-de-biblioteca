from pydantic import BaseModel, EmailStr, ConfigDict


class UsuarioBase(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str | None = None


class UsuarioCreate(UsuarioBase):
    senha: str
    tipo: str = "usuario"


class UsuarioResponse(UsuarioBase):
    id: int
    tipo: str

    model_config = ConfigDict(from_attributes=True)