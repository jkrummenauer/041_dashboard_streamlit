# src/validation.py

import pandas as pd

from src.config import COLUNAS_OBRIGATORIAS


def validar_colunas(df: pd.DataFrame) -> tuple[bool, list[str]]:
    """
    Verifica se todas as colunas obrigatórias existem no DataFrame.
    """

    colunas_faltantes = []

    for coluna in COLUNAS_OBRIGATORIAS:
        if coluna not in df.columns:
            colunas_faltantes.append(coluna)

    if colunas_faltantes:
        return False, colunas_faltantes

    return True, []