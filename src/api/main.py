from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.db import models
from src.db.database import SessionLocal, engine
from src.api import schemas
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/operadoras", response_model=list[schemas.OperadoraResponse])
def listar_operadoras(q: str = None, db: Session = Depends(get_db)):
    query_set = db.query(models.Operadora)
    if q:
        query_set = query_set.filter(models.Operadora.razao_social.ilike(f"%{q}%"))
    return query_set.all()

@app.get("/operadora/{registro_ans}", response_model=schemas.OperadoraResponse)
def buscar_operadora(registro_ans: int, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.registro_ans == registro_ans).first()
    if not operadora:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")
    return operadora

@app.post("/operadora", response_model=schemas.OperadoraResponse)
def criar_operadora(operadora: schemas.OperadoraSchema, db: Session = Depends(get_db)):
    nova_operadora = models.Operadora(**operadora.dict())
    db.add(nova_operadora)
    db.commit()
    db.refresh(nova_operadora)
    return nova_operadora

@app.put("/operadora/{registro_ans}", response_model=schemas.OperadoraResponse)
def atualizar_operadora(registro_ans: int, dados: schemas.OperadoraSchema, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.registro_ans == registro_ans).first()
    if not operadora:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")
    for chave, valor in dados.dict(exclude_unset=True).items():
        setattr(operadora, chave, valor)
    db.commit()
    db.refresh(operadora)
    return operadora

@app.delete("/operadora/{registro_ans}")
def deletar_operadora(registro_ans: int, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.registro_ans == registro_ans).first()
    if not operadora:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")
    db.delete(operadora)
    db.commit()
    return {"message": "Operadora deletada com sucesso."}
