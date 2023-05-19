from pydantic import BaseModel

class FormasEntregaSchema(BaseModel):
   id: int
   descricao: str

   class Config:
      orm_mode = True