"""Arquivo de Configuração do Contrato de Dados."""
from datetime import datetime

from pydantic import BaseModel, EmailStr, PositiveInt


class ContratoFuncionarios(BaseModel):
    """
    Classe de Contrato de Dados, recebendo o BaseModel do Pydantic.

    Args:
        id (int): Identificador do funcionário.
        nome (str): Nome do funcionário.
        datenascimento (datetime): Data de nascimento do funcionário.
        email (str): E-mail do funcionário.
        cargo (EmailStr): Cargo do funcionário.
        departamento (str): Departamento do funcionário.
    """

    id: PositiveInt
    nome: str
    idade: PositiveInt
    datanascimento: datetime
    email: EmailStr
    cargo: str
    departamento: str
