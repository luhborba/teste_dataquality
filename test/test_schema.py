"""Arquivo de Testes do Schema."""
import pytest
from pydantic import ValidationError
from datetime import datetime
from schema import ContratoFuncionarios


def test_dados_validos():
        """Função de teste com dados validos."""
        dados_validos = {
                "id": 1,
                "nome": "teste",
                "idade": 1,
                "datanascimento": datetime.now(),
                "email": "teste@email.com",
                "cargo": "teste",
                "departamento": "teste"
        }
        funcionarios = ContratoFuncionarios(**dados_validos)
        assert funcionarios.id == dados_validos["id"]
        assert funcionarios.nome == dados_validos["nome"]
        assert funcionarios.idade == dados_validos["idade"]
        assert funcionarios.datanascimento == dados_validos["datanascimento"]
        assert funcionarios.email == dados_validos["email"]
        assert funcionarios.cargo == dados_validos["cargo"]
        assert funcionarios.departamento == dados_validos["departamento"]

def test_dados_invalido():
    """Função de teste com dados invalidos."""
    dados_invalidos = {
        "id": -1,
        "nome": "teste",
        "idade": 1,
        "datanascimento": datetime.now(),
        "email": "teste",
        "cargo": "teste",
        "departamento": "teste"
    }
    with pytest.raises(ValidationError):
        ContratoFuncionarios(**dados_invalidos)