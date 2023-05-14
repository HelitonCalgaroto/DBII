from pydantic import BaseModel

class ComposicaoSchema(BaseModel):
    id: int
    produto_id: int
    descricao: str
    preco: float

    class Config:
        orm_mode = True