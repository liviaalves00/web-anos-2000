from sqlalchemy.orm import Session
from app.models.modelo import ModeloVeiculo
from app.schemas.modelo import ModeloVeiculoCreate, ModeloVeiculoUpdate

def create_modelo(db: Session, modelo: ModeloVeiculoCreate):
    db_modelo = ModeloVeiculo(**modelo.dict())
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)
    return db_modelo

def get_modelos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ModeloVeiculo).offset(skip).limit(limit).all()

def get_modelo(db: Session, modelo_id: str):
    return db.query(ModeloVeiculo).filter(ModeloVeiculo.id == modelo_id).first()

def update_modelo(db: Session, modelo_id: str, modelo_update: ModeloVeiculoUpdate):
    db_modelo = db.query(ModeloVeiculo).filter(ModeloVeiculo.id == modelo_id).first()
    if db_modelo:
        for key, value in modelo_update.dict(exclude_unset=True).items():
            setattr(db_modelo, key, value)
        db.commit()
        db.refresh(db_modelo)
        return db_modelo
    return None

def delete_modelo(db: Session, modelo_id: str):
    db_modelo = db.query(ModeloVeiculo).filter(ModeloVeiculo.id == modelo_id).first()
    if db_modelo:
        db.delete(db_modelo)
        db.commit()
        return db_modelo
    return None
