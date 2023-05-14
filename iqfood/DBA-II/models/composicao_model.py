from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings

class ComposicaoModel(settings.DBBaseModel):
    __tablename__ = 'composicao'

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    descricao = Column(String)
    preco = Column(Float)

    produto = relationship("Produto", back_populates="composicao")