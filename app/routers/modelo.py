from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import schemas, crud
from app.core.database import get_db
from app.crud import modelo as crud_modelo

router = APIRouter()

templates = Jinja2Templates(directory='app/templates')

# Criar um novo modelo de veículo
from fastapi import Form

@router.post("/modelos", response_model=schemas.modelo.ModeloVeiculoResponse)
def create_modelo(
    nome: str = Form(...),
    valor_referencia: float = Form(...),
    motorizacao: float = Form(...),
    turbo: bool = Form(False),
    automatico: bool = Form(False),
    montadora_id: int = Form(...),
    db: Session = Depends(get_db)
):
    modelo = schemas.modelo.ModeloVeiculoCreate(
        nome=nome,
        valor_referencia=valor_referencia,
        motorizacao=motorizacao,
        turbo=turbo,
        automatico=automatico,
        montadora_id=montadora_id
    )
    return crud_modelo.create_modelo(db=db, modelo=modelo)


# Listar todos os modelos de veículos com paginação
@router.get("/modelos", response_model=list[schemas.modelo.ModeloVeiculoResponse])
def get_modelos(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    modelos = crud_modelo.get_modelos(db=db, skip=skip, limit=limit)
    return templates.TemplateResponse(
        request=request, 
        name='modelos_list.html', 
        context={'modelos': modelos}
  )

@router.get("/modelos/form")
def get_modelos(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name='modelos_form.html', 
  )

# Obter um modelo de veículo específico pelo ID
@router.get("/modelos/{modelo_id}", response_model=schemas.modelo.ModeloVeiculoResponse)
def get_modelo(modelo_id: str, db: Session = Depends(get_db)):
    db_modelo = crud_modelo.get_modelo(db=db, modelo_id=modelo_id)
    if not db_modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    return db_modelo

# Atualizar um modelo de veículo existente pelo ID
@router.put("/modelos/{modelo_id}", response_model=schemas.modelo.ModeloVeiculoResponse)
def update_modelo(modelo_id: str, modelo_update: schemas.modelo.ModeloVeiculoUpdate, db: Session = Depends(get_db)):
    db_modelo = crud_modelo.update_modelo(db=db, modelo_id=modelo_id, modelo_update=modelo_update)
    if not db_modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado para atualização")
    return db_modelo

# Deletar um modelo de veículo pelo ID
@router.delete("/modelos/{modelo_id}", response_model=schemas.modelo.ModeloVeiculoResponse)
def delete_modelo(modelo_id: str, db: Session = Depends(get_db)):
    db_modelo = crud_modelo.delete_modelo(db=db, modelo_id=modelo_id)
    if not db_modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado para exclusão")
    return db_modelo
