from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class PedidoSchema(BaseModel):
    id: Optional[int] = None
    restaurante_id: int
    cliente_id: int
    formas_id: int
    formas_de_entrega_id: int
    endereco_id: int
    data: Optional[datetime] = None
    observacao: Optional[str] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True