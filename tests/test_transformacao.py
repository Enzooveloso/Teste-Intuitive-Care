import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from transformacao_dados.main import substituir_abreviacoes

def test_substituir_abreviacoes():
    df = pd.DataFrame({
        "Procedimento": ["Proc1", "Proc2"],
        "OD": ["OD", "OD"],
        "AMB": ["AMB", "AMB"]
    })

    df_modificado = substituir_abreviacoes(df)

    assert "OD" not in df_modificado["OD"].values
    assert "AMB" not in df_modificado["AMB"].values