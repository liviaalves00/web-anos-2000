# from ulid import ULID
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float
from app.core.database import Base
from sqlalchemy.orm import relationship
from app.models.montadora import Montadora


class ModeloVeiculo(Base):
    __tablename__ = "modelo"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    montadora_id = Column(Integer, ForeignKey("montadora.id"))
    valor_referencia = Column(Float)
    motorizacao = Column(Integer)
    turbo = Column(Boolean)
    automatico = Column(Boolean)

    montadora = relationship("Montadora", back_populates="models")
