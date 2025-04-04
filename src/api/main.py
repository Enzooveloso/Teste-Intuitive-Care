from fastapi import FastAPI, Depends, HTTPException
from src import schemas
from src.repository import operadora_repository
from src.db.unit_of_work import unit_of_work
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/operadoras", response_model=list[schemas.OperadoraResponse])
def listar_operadoras(q: str = None):
    with unit_of_work() as db:
        return operadora_repository.get_all(db, filtro=q)

@app.get("/operadora/{registro_ans}", response_model=schemas.OperadoraResponse)
def buscar_operadora(registro_ans: int):
    with unit_of_work() as db:
        operadora = operadora_repository.get_by_registro_ans(db, registro_ans)
        if not operadora:
            raise HTTPException(status_code=404, detail="Operadora não encontrada")
        return operadora

@app.post("/operadora", response_model=schemas.OperadoraResponse)
def criar_operadora(operadora: schemas.OperadoraSchema):
    with unit_of_work() as db:
        return operadora_repository.create(db, operadora)

@app.put("/operadora/{registro_ans}", response_model=schemas.OperadoraResponse)
def atualizar_operadora(registro_ans: int, dados: schemas.OperadoraSchema):
    with unit_of_work() as db:
        operadora = operadora_repository.update(db, registro_ans, dados)
        if not operadora:
            raise HTTPException(status_code=404, detail="Operadora não encontrada")
        return operadora

@app.delete("/operadora/{registro_ans}")
def deletar_operadora(registro_ans: int):
    with unit_of_work() as db:
        sucesso = operadora_repository.delete(db, registro_ans)
        if not sucesso:
            raise HTTPException(status_code=404, detail="Operadora não encontrada")
        return {"message": "Operadora deletada com sucesso."}