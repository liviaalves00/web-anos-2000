from fastapi import FastAPI

from .routers import modelo, montadora
# from app.routers. import montadora, veiculo

app = FastAPI()

# Registrar as rotas
app.include_router(montadora.router)
app.include_router(modelo.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao sistema PatroCars"}
