import sys
import os
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from api.main import app

client = TestClient(app)

def test_busca_operadora_existente():
    response = client.get("/operadoras?q=amil")
    assert response.status_code == 200
    dados = response.json()
    assert isinstance(dados, list)
    assert any("amil" in op["razao_social"].lower() for op in dados)

def test_busca_operadora_inexistente():
    response = client.get("/operadoras?q=naoencontravel123")
    assert response.status_code == 200
    dados = response.json()
    assert isinstance(dados, list)
    assert len(dados) == 0

def test_parametro_vazio():
    response = client.get("/operadoras?q=")
    assert response.status_code == 422
