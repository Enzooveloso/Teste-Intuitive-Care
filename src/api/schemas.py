from pydantic import BaseModel
from typing import Optional

class OperadoraSchema(BaseModel):
    registro_ans: int
    cnpj: Optional[str] = None
    razao_social: Optional[str] = None
    modalidade: Optional[str] = None
    uf: Optional[str] = None
    municipio: Optional[str] = None
    data_registro: Optional[str] = None

class OperadoraResponse(OperadoraSchema):
    class Config:
        orm_mode = True
