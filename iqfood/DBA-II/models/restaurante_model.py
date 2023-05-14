from sqlalchemy import Column, Integer, String, Float, ARRAY
from core.configs import settings

class RestauranteModel(settings.DBBaseModel):
    __tablename__ = 'restaurante'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    avaliacao = Column(Float)
    valor_minimo = Column(Float)
    horarios_funcionamento = Column(String)
    formas_entrega = Column(ARRAY(String))
    formas_pagamento = Column(ARRAY(String))
    categorias = Column(ARRAY(String))