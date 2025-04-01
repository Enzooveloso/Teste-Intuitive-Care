import sys
import os
import pytest
from fastapi.testclient import TestClient


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from api.main import app

client = TestClient(app)

def test_get_operadoras():
    response = client.get("/operadoras?q=amil")
    assert response.status_code == 200
    dados = response.json()
    assert isinstance(dados, list)
    if dados:
        assert "razao_social" in dados[0]

def test_get_operadora_by_id():
    response = client.get("/operadora/347237")
    assert response.status_code in (200, 404)
    if response.status_code == 200:
        operadora = response.json()
        assert "registro_ans" in operadora
        assert "razao_social" in operadora

def test_post_operadora():
    nova_operadora = {
        "registro_ans": 999999,
        "cnpj": "12345678900000",
        "razao_social": "Operadora de Teste",
        "modalidade": "Odontologia de Grupo",
        "uf": "MG",
        "municipio": "Montes Claros",
        "data_registro": "2025-01-01"
    }
    response = client.post("/operadora", json=nova_operadora)
    assert response.status_code in (200, 400)
    if response.status_code == 200:
        operadora = response.json()
        assert operadora["registro_ans"] == 999999

def test_delete_operadora():
    response = client.delete("/operadora/999999")
    assert response.status_code in (200, 404)
    if response.status_code == 200:
        assert response.json()["message"] == "Operadora deletada com sucesso."
