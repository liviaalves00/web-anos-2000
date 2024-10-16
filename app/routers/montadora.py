from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.crud import montadora as crud_montadora
from app.core.database import get_db

router = APIRouter()

@router.post("/create_montadora", response_model=schemas.montadora.MontadoraResponse)
def create_montadora(montadora: schemas.montadora.MontadoraCreate, db: Session = Depends(get_db)):
    # return crud.create_montadora(db=db, montadora=montadora)
    return crud_montadora.create_montadora(db=db, montadora=montadora)

