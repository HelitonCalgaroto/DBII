from pydantic import BaseModel

class FormasPagamentoSchema(BaseModel):
   id: int
   descricao: str

   class Config:
      orm_mode = True