from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.configs import settings

class ProdutoFotosModel(settings.DBBaseModel):
   __tablename__ = 'produto_fotos'
   
   id = Column(Integer, primary_key=True, autoincrement=True)
   url = Column(String(100))
   descricao = Column(String(30))
   data = Column(TIMESTAMP)
   produto_id = Column(Integer, ForeignKey('produto.id'))
   produto = relationship("Produto", back_populates="fotos")