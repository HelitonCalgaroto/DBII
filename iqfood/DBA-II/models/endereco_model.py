from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings

class EnderecoModel(settings.DBBaseModel):
    __tablename__ = "enderecos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    rua = Column(String(100))
    numero = Column(String(10))
    bairro = Column(String(50))
    cidade = Column(String(50))
    cep = Column(String(10))
    referencia = Column(String(100))
    latitude = Column(Float)
    longitude = Column(Float)

    cliente = relationship("Cliente", back_populates="enderecos")