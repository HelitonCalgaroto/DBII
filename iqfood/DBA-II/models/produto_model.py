from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text, Boolean, SmallInteger
from sqlalchemy.orm import relationship
from core.configs import settings

class ProdutoModel(settings.DBBaseModel):
   __tablename__ = 'produtos'

   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String(150), nullable=True)
   descricao = Column(Text)
   preco = Column(Numeric(15,2))
   fracionado = Column(Boolean, default=False)
   avaliacao = Column(SmallInteger, default=5)
   tamanho = Column(String(20))
   restaurante_id = Column(Integer, ForeignKey("restaurantes.id"))
   categoria_id = Column(Integer, ForeignKey('categoria.id'))

   restaurante = relationship("Restaurante", back_populates="produtos")
   categoria = relationship("CategoriaModel", back_populates='produtos', lazy='joined')
   fotos = relationship("ProdutoFotosModel", back_populates='produto_fotos', lazy='joined')