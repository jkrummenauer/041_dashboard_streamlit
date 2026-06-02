# src/data_processing.py

import pandas as pd

from src.config import COLUNAS_NUMERICAS


def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza tipos, remove dados inválidos e cria colunas auxiliares.
    """

    df = df.copy()

    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    for coluna in COLUNAS_NUMERICAS:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")

    df["fornecedor"] = df["fornecedor"].astype(str).str.strip()
    df["tipo_mercadoria"] = df["tipo_mercadoria"].astype(str).str.strip()
    df["conferente"] = df["conferente"].astype(str).str.strip()
    df["conferencia_id"] = df["conferencia_id"].astype(str).str.strip()

    df = df.dropna(subset=["data"])
    df = df.dropna(subset=COLUNAS_NUMERICAS)

    df = df[df["tempo_minutos"] > 0]
    df = df[df["volume_conferido"] >= 0]
    df = df[df["divergencias"] >= 0]

    df["ano"] = df["data"].dt.year
    df["mes"] = df["data"].dt.to_period("M").astype(str)
    df["dia"] = df["data"].dt.date
    df["semana"] = df["data"].dt.isocalendar().week
    df["horas"] = df["tempo_minutos"] / 60
    df["volume_por_hora"] = df["volume_conferido"] / df["horas"]

    df["tem_divergencia"] = df["divergencias"].apply(
        lambda valor: "Sim" if valor > 0 else "Não"
    )

    return df


def aplicar_filtros(
    df: pd.DataFrame,
    periodo,
    fornecedores_selecionados: list[str],
    tipos_selecionados: list[str],
    conferentes_selecionados: list[str],
) -> pd.DataFrame:
    """
    Aplica filtros de período, fornecedor, tipo de mercadoria e conferente.
    """

    df_filtrado = df.copy()

    if len(periodo) == 2:
        data_inicio = pd.to_datetime(periodo[0])
        data_fim = pd.to_datetime(periodo[1])

        df_filtrado = df_filtrado[
            (df_filtrado["data"] >= data_inicio)
            & (df_filtrado["data"] <= data_fim)
        ]

    df_filtrado = df_filtrado[
        (df_filtrado["fornecedor"].isin(fornecedores_selecionados))
        & (df_filtrado["tipo_mercadoria"].isin(tipos_selecionados))
        & (df_filtrado["conferente"].isin(conferentes_selecionados))
    ]

    return df_filtrado