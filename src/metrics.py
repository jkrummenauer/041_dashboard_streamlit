# src/metrics.py

import pandas as pd


def calcular_kpis(df: pd.DataFrame) -> dict:
    """
    Calcula os principais indicadores do dashboard.
    """

    if df.empty:
        return {
            "volume_total": 0,
            "quantidade_conferencias": 0,
            "tempo_medio": 0,
            "produtividade_media": 0,
            "divergencias_total": 0,
            "taxa_divergencia": 0,
        }

    volume_total = df["volume_conferido"].sum()
    quantidade_conferencias = df["conferencia_id"].nunique()
    tempo_medio = df["tempo_minutos"].mean()
    divergencias_total = df["divergencias"].sum()

    tempo_total_horas = df["tempo_minutos"].sum() / 60

    if tempo_total_horas > 0:
        produtividade_media = volume_total / tempo_total_horas
    else:
        produtividade_media = 0

    if quantidade_conferencias > 0:
        taxa_divergencia = divergencias_total / quantidade_conferencias
    else:
        taxa_divergencia = 0

    return {
        "volume_total": volume_total,
        "quantidade_conferencias": quantidade_conferencias,
        "tempo_medio": tempo_medio,
        "produtividade_media": produtividade_media,
        "divergencias_total": divergencias_total,
        "taxa_divergencia": taxa_divergencia,
    }


def calcular_ranking_conferentes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula ranking de produtividade por conferente.
    """

    if df.empty:
        return pd.DataFrame()

    ranking = (
        df.groupby("conferente")
        .agg(
            volume_total=("volume_conferido", "sum"),
            quantidade_conferencias=("conferencia_id", "nunique"),
            tempo_total_minutos=("tempo_minutos", "sum"),
            tempo_medio_minutos=("tempo_minutos", "mean"),
            divergencias_total=("divergencias", "sum"),
        )
        .reset_index()
    )

    ranking["horas_trabalhadas"] = ranking["tempo_total_minutos"] / 60

    ranking["volume_por_hora"] = (
        ranking["volume_total"] / ranking["horas_trabalhadas"]
    )

    ranking["divergencias_por_conferencia"] = (
        ranking["divergencias_total"] / ranking["quantidade_conferencias"]
    )

    ranking["score_produtividade"] = (
        ranking["volume_por_hora"] * 0.7
        - ranking["divergencias_por_conferencia"] * 10
    )

    ranking = ranking.sort_values(
        by="score_produtividade",
        ascending=False,
    )

    ranking.insert(0, "posicao", range(1, len(ranking) + 1))

    return ranking


def calcular_fornecedores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula indicadores agrupados por fornecedor.
    """

    if df.empty:
        return pd.DataFrame()

    fornecedores = (
        df.groupby("fornecedor")
        .agg(
            volume_total=("volume_conferido", "sum"),
            quantidade_conferencias=("conferencia_id", "nunique"),
            tempo_medio_minutos=("tempo_minutos", "mean"),
            divergencias_total=("divergencias", "sum"),
        )
        .reset_index()
    )

    fornecedores["divergencias_por_conferencia"] = (
        fornecedores["divergencias_total"]
        / fornecedores["quantidade_conferencias"]
    )

    fornecedores = fornecedores.sort_values(
        by="divergencias_total",
        ascending=False,
    )

    return fornecedores


def formatar_numero(valor: float) -> str:
    """
    Formata número no padrão brasileiro.
    """

    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_inteiro(valor: float) -> str:
    """
    Formata número inteiro no padrão brasileiro.
    """

    return f"{valor:,.0f}".replace(",", ".")