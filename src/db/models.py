from sqlalchemy import Column, Integer, String
from src.db.database import Base

class Operadora(Base):
    __tablename__ = "operadoras"

    registro_ans = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(20), nullable=True)
    razao_social = Column(String(255), nullable=True)
    modalidade = Column(String(100), nullable=True)
    uf = Column(String(2), nullable=True)
    municipio = Column(String(100), nullable=True)
    data_registro = Column(String(20), nullable=True) 
