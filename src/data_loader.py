# src/data_loader.py

import pandas as pd


def carregar_arquivo(arquivo) -> pd.DataFrame:
    """
    Carrega arquivo CSV ou Excel enviado pelo usuário.
    """

    nome_arquivo = arquivo.name.lower()

    if nome_arquivo.endswith(".csv"):
        return pd.read_csv(arquivo)

    if nome_arquivo.endswith(".xlsx"):
        return pd.read_excel(arquivo)

    raise ValueError("Formato de arquivo não suportado. Use CSV ou XLSX.")