from sqlalchemy import Column, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from core.configs import settings

pedido_produtos_composicoes_associacao = Table('pedido_produtos_composicoes', settings.DBBaseModel.metadata,
                                                Column('pedido_produtos_id', Integer, ForeignKey('pedido_produtos.id')),
                                                Column('composicao_id', Integer, ForeignKey('composicao.id')))

class PedidoProdutosComposicaoModel(settings.DBBaseModel):
    __tablename__ = 'pedido_produtos'

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey('produto.id'))
    pedido_id = Column(Integer, ForeignKey('pedido.id'))
    quantidade = Column(Integer)
    valor = Column(Float)
    composicoes = relationship('Composicao', secondary=pedido_produtos_composicoes_associacao, backref='pedido_produtos')

    produto = relationship('Produto', back_populates='pedido_produtos')
    pedido = relationship('Pedido', back_populates='pedido_produtos')