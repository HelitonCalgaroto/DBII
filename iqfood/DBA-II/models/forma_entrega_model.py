from sqlalchemy import Column, Integer, String
from core.configs import settings

class FormasEntrega(settings.DBBaseModel):
   __tablename__ = 'formas_entrega'

   id = Column(Integer, primary_key=True, index=True)
   descricao = Column(String(255), nullable=False)