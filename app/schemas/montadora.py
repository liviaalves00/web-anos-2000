from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional
from .modelo import ModeloVeiculoResponse 
class MontadoraBase(BaseModel):
    nome: str
    pais: str
    ano_fundacao: int

class MontadoraCreate(MontadoraBase):
    pass

class MontadoraUpdate(BaseModel):
    nome: Optional[str]
    pais: Optional[str]
    ano_fundacao: Optional[int]

class MontadoraResponse(MontadoraBase):
    id: int 
    modelos: List[ModeloVeiculoResponse] = []

    class Config:
        orm_mode = True
