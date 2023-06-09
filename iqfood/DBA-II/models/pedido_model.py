from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from core.configs import settings


class PedidoModel(settings.DBBaseModel):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, index=True)
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'))
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    formas_id = Column(Integer, ForeignKey('formas_pagamento.id'))
    formas_de_entrega_id = Column(Integer, ForeignKey('formas_entrega.id'))
    endereco_id = Column(Integer, ForeignKey('endereco.id'))
    data = Column(DateTime)
    observacao = Column(String(255), nullable=True)
    status = Column(String(50))

    restaurante = relationship('Restaurante', back_populates='pedidos')
    cliente = relationship('Cliente', back_populates='pedidos')
    formas_pagamento = relationship('FormasPagamento', back_populates='pedidos')
    formas_entrega = relationship('FormasEntrega', back_populates='pedidos')
    endereco = relationship('Endereco', back_populates='pedidos')