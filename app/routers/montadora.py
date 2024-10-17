from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.crud import montadora as crud_montadora
from app.core.database import get_db

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import schemas, crud
from app.core.database import get_db
from app.crud import montadora as crud_montadora
from fastapi import Form
from fastapi.responses import RedirectResponse

router = APIRouter()

templates = Jinja2Templates(directory='app/templates')

# Listar todas as montadoras com paginação
@router.get("/montadoras", response_model=list[schemas.montadora.MontadoraResponse])
def get_montadoras(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    montadoras = crud_montadora.get_montadoras(db=db, skip=skip, limit=limit)
    return templates.TemplateResponse(
        request=request,
        name='montadoras_list.html',
        context={'montadoras': montadoras}
    )

@router.get("/montadoras/form", response_model=schemas.montadora.MontadoraResponse)
def get_montadora_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='montadoras_form.html',
    )

@router.post("/montadoras", response_model=schemas.montadora.MontadoraResponse)
def create_montadora(
    nome: str = Form(...),
    pais: str = Form(...),
    ano_fundacao: int = Form(...),
    db: Session = Depends(get_db)
):
    montadora = schemas.montadora.MontadoraCreate(nome=nome, pais=pais, ano_fundacao=ano_fundacao)
    return crud_montadora.create_montadora(db=db, montadora=montadora)

@router.get("/montadoras/{montadora_id}", response_model=schemas.montadora.MontadoraResponse)
def get_montadora(montadora_id: str, db: Session = Depends(get_db)):
    db_montadora = crud_montadora.get_montadora(db=db, montadora_id=montadora_id)
    if not db_montadora:
        raise HTTPException(status_code=404, detail="Montadora não encontrada")
    return db_montadora

# Obter uma montadora específica pelo ID
@router.get("/montadoras/form/{montadora_id}")
def get_montadora_edit_form(montadora_id: str, request: Request, db: Session = Depends(get_db)):
    db_montadora = crud_montadora.get_montadora(db=db, montadora_id=montadora_id)
    if not db_montadora:
        raise HTTPException(status_code=404, detail="Montadora não encontrada")
    
    return templates.TemplateResponse(
        name='montadoras_edit.html',
        context={'request': request, 'montadora': db_montadora}
    )
# Atualizar uma montadora existente pelo ID

@router.post("/montadoras/form/{montadora_id}", response_model=schemas.montadora.MontadoraResponse)
def update_montadora(
    montadora_id: str,
    nome: str = Form(...),
    pais: str = Form(...),
    ano_fundacao: int = Form(...),
    db: Session = Depends(get_db)
):
    montadora_update = schemas.montadora.MontadoraUpdate(
        nome=nome,
        pais=pais,
        ano_fundacao=ano_fundacao
    )

    db_montadora = crud_montadora.update_montadora(
        db=db,
        montadora_id=montadora_id,
        montadora_update=montadora_update
    )

    if not db_montadora:
        raise HTTPException(status_code=404, detail="Montadora não encontrada para atualização")

    # Redirecionar para a lista de montadoras após a atualização
    return RedirectResponse(url='/montadoras', status_code=303)

# Deletar uma montadora pelo ID
@router.post("/montadoras/delete/{montadora_id}", response_model=schemas.montadora.MontadoraResponse)
def delete_montadora(montadora_id: str, db: Session = Depends(get_db)):
    db_montadora = crud_montadora.delete_montadora(db=db, montadora_id=montadora_id)
    if not db_montadora:
        raise HTTPException(status_code=404, detail="Montadora não encontrada para exclusão")
    return RedirectResponse(url='/montadoras', status_code=303)
