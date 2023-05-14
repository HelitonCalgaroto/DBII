from typing import Optional
from pydantic import BaseModel

class ClienteSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    email: str
    cpf: str
    login: str
    senha: str

    class Config:
        orm_mode = True