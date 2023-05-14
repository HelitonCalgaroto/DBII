from typing import List
from pydantic import BaseModel

class PedidoProdutosSchema(BaseModel):
    id: int
    produto_id: int
    pedido_id: int
    quantidade: int
    valor: float
    composicoes: List[int] = []

    class Config:
        orm_mode = True