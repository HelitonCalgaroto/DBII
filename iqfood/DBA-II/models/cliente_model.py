from sqlalchemy import Column, Integer, String
from core.configs import settings

class ClienteModel(settings.DBBaseModel):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    telefone = Column(String(20))
    email = Column(String(100), unique=True, index=True)
    cpf = Column(String(14), unique=True, index=True)
    login = Column(String(20), unique=True, index=True)
    senha = Column(String(100))