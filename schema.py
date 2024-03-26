"""Arquivo de Configuração do Contrato de Dados."""
from datetime import datetime

from pydantic import BaseModel, EmailStr, PositiveInt


class ContratoFuncionarios(BaseModel):
    """
    Classe de Contrato de Dados, recebendo o BaseModel do Pydantic.

    Args:
        BaseModel: Classe base do Pydantic.
    """
    
    id: PositiveInt
    nome: str
    idade: PositiveInt
    datanascimento: datetime
    email: EmailStr
    cargo: str
    departamento: str
