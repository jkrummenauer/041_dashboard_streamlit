# src/charts.py

import pandas as pd
import plotly.express as px


def grafico_volume_por_dia(df: pd.DataFrame):
    volume_por_dia = (
        df.groupby("dia")
        .agg(volume_total=("volume_conferido", "sum"))
        .reset_index()
    )

    fig = px.line(
        volume_por_dia,
        x="dia",
        y="volume_total",
        markers=True,
        title="Volume Conferido por Dia",
    )

    return fig


def grafico_conferencias_por_dia(df: pd.DataFrame):
    conferencias_por_dia = (
        df.groupby("dia")
        .agg(quantidade_conferencias=("conferencia_id", "nunique"))
        .reset_index()
    )

    fig = px.bar(
        conferencias_por_dia,
        x="dia",
        y="quantidade_conferencias",
        title="Quantidade de Conferências por Dia",
    )

    return fig


def grafico_volume_por_tipo(df: pd.DataFrame):
    volume_por_tipo = (
        df.groupby("tipo_mercadoria")
        .agg(volume_total=("volume_conferido", "sum"))
        .reset_index()
        .sort_values(by="volume_total", ascending=False)
    )

    fig = px.pie(
        volume_por_tipo,
        names="tipo_mercadoria",
        values="volume_total",
        title="Participação por Tipo de Mercadoria",
    )

    return fig


def grafico_tempo_por_tipo(df: pd.DataFrame):
    tempo_por_tipo = (
        df.groupby("tipo_mercadoria")
        .agg(tempo_medio=("tempo_minutos", "mean"))
        .reset_index()
        .sort_values(by="tempo_medio", ascending=False)
    )

    fig = px.bar(
        tempo_por_tipo,
        x="tipo_mercadoria",
        y="tempo_medio",
        title="Tempo Médio por Tipo de Mercadoria",
    )

    return fig


def grafico_ranking_volume_por_hora(ranking: pd.DataFrame):
    fig = px.bar(
        ranking,
        x="conferente",
        y="volume_por_hora",
        text="volume_por_hora",
        title="Ranking por Volume por Hora",
    )

    fig.update_traces(
        texttemplate="%{text:.1f}",
        textposition="outside",
    )

    return fig


def grafico_divergencias_por_conferente(ranking: pd.DataFrame):
    df_grafico = ranking.sort_values(
        by="divergencias_por_conferencia",
        ascending=False,
    )

    fig = px.bar(
        df_grafico,
        x="conferente",
        y="divergencias_por_conferencia",
        text="divergencias_por_conferencia",
        title="Divergências por Conferência",
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside",
    )

    return fig


def grafico_volume_tempo_conferente(ranking: pd.DataFrame):
    fig = px.scatter(
        ranking,
        x="tempo_total_minutos",
        y="volume_total",
        size="quantidade_conferencias",
        color="conferente",
        hover_name="conferente",
        title="Volume Total x Tempo Total por Conferente",
    )

    return fig


def grafico_volume_por_fornecedor(fornecedores: pd.DataFrame):
    df_grafico = fornecedores.sort_values(
        by="volume_total",
        ascending=False,
    )

    fig = px.bar(
        df_grafico,
        x="fornecedor",
        y="volume_total",
        title="Volume Total por Fornecedor",
    )

    return fig


def grafico_divergencias_por_fornecedor(fornecedores: pd.DataFrame):
    df_grafico = fornecedores.sort_values(
        by="divergencias_total",
        ascending=False,
    )

    fig = px.bar(
        df_grafico,
        x="fornecedor",
        y="divergencias_total",
        title="Divergências por Fornecedor",
    )

    return fig