from typing import Optional
from pydantic import BaseModel, HttpUrl
from datetime import datetime

class ProdutoFotosSchema(BaseModel):
   id = Optional[int] = None
   produto_id = Optional[int]
   url = HttpUrl
   descricao = str
   ata: datetime.datetime
   
   class Config:
      orm_mode = True