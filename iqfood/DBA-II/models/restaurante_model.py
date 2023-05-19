from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings

restaurante_formas_entrega = Table('restaurante_formas_entrega', settings.DBBaseModel.metadata,
    Column('restaurante_id', Integer, ForeignKey('restaurante.id'), primary_key=True),
    Column('formas_entrega_id', Integer, ForeignKey('formas_entrega.id'), primary_key=True)
)

restaurante_formas_pagamento = Table('restaurante_formas_pagamento', settings.DBBaseModel.metadata,
    Column('restaurante_id', Integer, ForeignKey('restaurante.id'), primary_key=True),
    Column('formas_pagamento_id', Integer, ForeignKey('formas_pagamento.id'), primary_key=True)
)

class RestauranteModel(settings.DBBaseModel):
    __tablename__ = 'restaurante'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String(255), nullable=False)
    telefone = Column(String(20), nullable=False)
    avaliacao = Column(Integer)
    valor_minimo = Column(Integer)
    horarios_funcionamento = Column(String(255))
    formas_pagamento = relationship('FormasPagamento', secondary=restaurante_formas_pagamento, back_populates='restaurantes')
    formas_entrega = relationship('FormasEntrega', secondary=restaurante_formas_entrega, back_populates='restaurantes')
    categorias = relationship('Categoria', back_populates='restaurante')