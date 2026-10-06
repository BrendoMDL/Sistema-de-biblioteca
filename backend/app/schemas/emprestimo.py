from datetime import date

from pydantic import BaseModel, ConfigDict


class EmprestimoCreate(BaseModel):
    usuario_id: int
    livro_id: int
    data_prevista_devolucao: date


class EmprestimoResponse(BaseModel):
    id: int
    usuario_id: int
    livro_id: int
    data_emprestimo: date
    data_prevista_devolucao: date
    data_devolucao: date | None = None
    status: str

    model_config = ConfigDict(from_attributes=True)