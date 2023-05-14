from typing import Optional, List
from pydantic import BaseModel

class RestauranteSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    endereco: str
    telefone: str
    avaliacao: float
    valor_minimo: float
    horarios_funcionamento: str
    formas_entrega: List[str]
    formas_pagamento: List[str]
    categorias: List[str]

    class Config:
        orm_mode = True