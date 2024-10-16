from pydantic import BaseModel
from typing import Optional

class ModeloVeiculoBase(BaseModel):
    nome: str
    valor_referencia: float
    motorizacao: float
    turbo: bool
    automatico: bool

class ModeloVeiculoCreate(ModeloVeiculoBase):
    montadora_id: int 

class ModeloVeiculoUpdate(BaseModel):
    nome: Optional[str]
    valor_referencia: Optional[float]
    motorizacao: Optional[float]
    turbo: Optional[bool]
    automatico: Optional[bool]

class ModeloVeiculoResponse(ModeloVeiculoBase):
    id: int
    montadora_id: int

    class Config:
        orm_mode = True
