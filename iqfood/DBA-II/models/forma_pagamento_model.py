from sqlalchemy import Column, Integer, String
from core.configs import settings

class FormasPagamento(settings.DBBaseModel):
   __tablename__ = 'formas_pagamento'

   id = Column(Integer, primary_key=True, index=True)
   descricao = Column(String(255), nullable=False)