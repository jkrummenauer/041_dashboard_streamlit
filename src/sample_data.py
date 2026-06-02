# src/sample_data.py

import pandas as pd

from src.config import COLUNAS_OBRIGATORIAS


def gerar_base_exemplo() -> pd.DataFrame:
    """
    Gera uma base de exemplo para testar o dashboard.
    """

    dados = [
        ["2026-06-01", "CONF-1001", "Fornecedor A", "Mercearia", "Carlos", 120, 45, 2],
        ["2026-06-01", "CONF-1002", "Fornecedor B", "Frios", "Ana", 80, 35, 0],
        ["2026-06-01", "CONF-1003", "Fornecedor C", "Hortifruti", "João", 150, 60, 4],
        ["2026-06-02", "CONF-1004", "Fornecedor A", "Mercearia", "Ana", 130, 50, 1],
        ["2026-06-02", "CONF-1005", "Fornecedor B", "Frios", "Carlos", 90, 40, 3],
        ["2026-06-02", "CONF-1006", "Fornecedor D", "Bebidas", "João", 200, 70, 2],
        ["2026-06-03", "CONF-1007", "Fornecedor A", "Mercearia", "Ana", 160, 55, 0],
        ["2026-06-03", "CONF-1008", "Fornecedor C", "Hortifruti", "Carlos", 110, 48, 2],
        ["2026-06-03", "CONF-1009", "Fornecedor D", "Bebidas", "João", 210, 75, 5],
        ["2026-06-04", "CONF-1010", "Fornecedor E", "Limpeza", "Marcos", 140, 50, 1],
        ["2026-06-04", "CONF-1011", "Fornecedor A", "Mercearia", "Carlos", 180, 65, 0],
        ["2026-06-04", "CONF-1012", "Fornecedor B", "Frios", "Ana", 95, 42, 2],
        ["2026-06-05", "CONF-1013", "Fornecedor C", "Hortifruti", "Marcos", 170, 68, 4],
        ["2026-06-05", "CONF-1014", "Fornecedor D", "Bebidas", "João", 230, 80, 3],
        ["2026-06-05", "CONF-1015", "Fornecedor E", "Limpeza", "Ana", 125, 47, 1],
        ["2026-06-06", "CONF-1016", "Fornecedor A", "Mercearia", "Marcos", 155, 60, 2],
        ["2026-06-06", "CONF-1017", "Fornecedor B", "Frios", "Carlos", 100, 38, 1],
        ["2026-06-06", "CONF-1018", "Fornecedor D", "Bebidas", "João", 250, 85, 4],
    ]

    df = pd.DataFrame(dados, columns=COLUNAS_OBRIGATORIAS)
    df["data"] = pd.to_datetime(df["data"])

    return df