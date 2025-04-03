from sqlalchemy.orm import Session
from src.db.models import Operadora
from src.api.schemas import OperadoraSchema


def get_all(db: Session, filtro: str | None = None) -> list[Operadora]:
    query = db.query(Operadora)
    if filtro:
        query = query.filter(Operadora.razao_social.ilike(f"%{filtro}%"))
    return query.all()


def get_by_registro_ans(db: Session, registro_ans: int) -> Operadora | None:
    return db.query(Operadora).filter(Operadora.registro_ans == registro_ans).first()


def create(db: Session, dados: OperadoraSchema) -> Operadora:
    nova = Operadora(**dados.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


def update(db: Session, registro_ans: int, dados: OperadoraSchema) -> Operadora | None:
    operadora = get_by_registro_ans(db, registro_ans)
    if not operadora:
        return None
    for chave, valor in dados.dict(exclude_unset=True).items():
        setattr(operadora, chave, valor)
    db.commit()
    db.refresh(operadora)
    return operadora


def delete(db: Session, registro_ans: int) -> bool:
    operadora = get_by_registro_ans(db, registro_ans)
    if not operadora:
        return False
    db.delete(operadora)
    db.commit()
    return True
