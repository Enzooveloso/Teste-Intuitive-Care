from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.db import models
from src.db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/operadoras")
def listar_operadoras(db: Session = Depends(get_db)):
    return db.query(models.Operadora).all()

@app.get("/operadoras/{registro_ans}")
def buscar_operadora(registro_ans: int, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.registro_ans == registro_ans).first()
    if not operadora:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")
    return operadora

@app.post("/operadoras")
def criar_operadora(operadora: dict, db: Session = Depends(get_db)):
    nova_operadora = models.Operadora(**operadora)
    db.add(nova_operadora)
    db.commit()
    db.refresh(nova_operadora)
    return nova_operadora

@app.put("/operadoras/{registro_ans}")
def atualizar_operadora(registro_ans: int, dados: dict, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.registro_ans == registro_ans).first()
    if not operadora:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")
    for chave, valor in dados.items():
        setattr(operadora, chave, valor)
    db.commit()
    db.refresh(operadora)
    return operadora

@app.delete("/operadoras/{registro_ans}")
def deletar_operadora(registro_ans: int, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.registro_ans == registro_ans).first()
    if not operadora:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")
    db.delete(operadora)
    db.commit()
    return {"mensagem": "Operadora deletada com sucesso"}
