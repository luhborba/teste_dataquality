from pydantic import BaseModel, PositiveInt, EmailStr
from datetime import datetime

class ContratoFuncionarios(BaseModel):
    id: PositiveInt
    nome: str
    idade: PositiveInt
    datanascimento: datetime
    email: EmailStr
    cargo: str
    departamento: str