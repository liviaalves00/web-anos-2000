# from ulid import ULID
from sqlalchemy import Column, String, Integer
from app.core.database import Base
from sqlalchemy.orm import relationship

class Montadora(Base):
    __tablename__ = "montadora"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    pais = Column(String)
    ano_fundacao = Column(Integer)

    models = relationship("ModeloVeiculo", back_populates="montadora")