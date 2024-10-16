from sqlalchemy.orm import Session
from app.models.montadora import Montadora
from app.schemas.montadora import MontadoraCreate, MontadoraUpdate

def create_montadora(db: Session, montadora: MontadoraCreate):
    db_montadora = Montadora(**montadora.dict())
    db.add(db_montadora)
    db.commit()
    db.refresh(db_montadora)
    return db_montadora

def get_montadoras(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Montadora).offset(skip).limit(limit).all()

def get_montadora(db: Session, montadora_id: str):
    return db.query(Montadora).filter(Montadora.id == montadora_id).first()

def update_montadora(db: Session, montadora_id: str, montadora_update: MontadoraUpdate):
    db_montadora = db.query(Montadora).filter(Montadora.id == montadora_id).first()
    if db_montadora:
        for key, value in montadora_update.dict(exclude_unset=True).items():
            setattr(db_montadora, key, value)
        db.commit()
        db.refresh(db_montadora)
        return db_montadora
    return None

def delete_montadora(db: Session, montadora_id: str):
    db_montadora = db.query(Montadora).filter(Montadora.id == montadora_id).first()
    if db_montadora:
        db.delete(db_montadora)
        db.commit()
        return db_montadora
    return None
