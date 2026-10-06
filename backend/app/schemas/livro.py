from pydantic import BaseModel, ConfigDict, Field


class LivroBase(BaseModel):
    titulo: str
    autor: str
    isbn: str
    editora: str | None = None
    ano_publicacao: int | None = None
    categoria: str | None = None
    quantidade: int = Field(ge=0)
    descricao: str | None = None


class LivroCreate(LivroBase):
    pass


class LivroUpdate(BaseModel):
    titulo: str | None = None
    autor: str | None = None
    isbn: str | None = None
    editora: str | None = None
    ano_publicacao: int | None = None
    categoria: str | None = None
    quantidade: int | None = Field(default=None, ge=0)
    descricao: str | None = None


class LivroResponse(LivroBase):
    id: int

    model_config = ConfigDict(from_attributes=True)