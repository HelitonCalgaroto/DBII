from typing import Optional
from pydantic import BaseModel

class EnderecoSchema(BaseModel):
    id: Optional[int] = None
    cliente_id: int
    rua: str
    numero: str
    bairro: str
    cidade: str
    cep: str
    referencia: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    class Config:
        orm_mode = True