from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from core.configs import settings


class PedidoModel(settings.DBBaseModel):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    restaurante_id = Column(Integer, ForeignKey("restaurantes.id"))
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    formas_id = Column(Integer, ForeignKey("formas_pagamento.id"))
    formas_de_entrega_id = Column(Integer, ForeignKey("formas_entrega.id"))
    endereco_id = Column(Integer, ForeignKey("enderecos.id"))
    data = Column(DateTime, default=datetime.utcnow)
    observacao = Column(String(255), nullable=True)
    status = Column(String(20), nullable=True)

    restaurante = relationship("Restaurante", back_populates="pedidos")
    cliente = relationship("Cliente", back_populates="pedidos")
    formas_pagamento = relationship("FormaPagamento", back_populates="pedidos")
    formas_entrega = relationship("FormaEntrega", back_populates="pedidos")
    endereco = relationship("Endereco", back_populates="pedidos")
    itens_pedido = relationship("ItemPedido", back_populates="pedido")