from datetime import datetime
import streamlit as st
from src.charts import (
    grafico_conferencias_por_dia,
    grafico_divergencias_por_conferente,
    grafico_divergencias_por_fornecedor,
    grafico_ranking_volume_por_hora,
    grafico_tempo_por_tipo,
    grafico_volume_por_dia,
    grafico_volume_por_fornecedor,
    grafico_volume_por_tipo,
    grafico_volume_tempo_conferente,
)
from src.config import (
    COLUNAS_OBRIGATORIAS,
    PAGE_ICON,
    PAGE_TITLE,
)
from src.data_loader import carregar_arquivo
from src.data_processing import aplicar_filtros, tratar_dados
from src.export import converter_df_para_excel
from src.metrics import (
    calcular_fornecedores,
    calcular_kpis,
    calcular_ranking_conferentes,
    formatar_inteiro,
    formatar_numero,
)
from src.sample_data import gerar_base_exemplo
from src.validation import validar_colunas

# Pagina inicial
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
)


# ============================================================
# CABEÇALHO
# ============================================================

st.title(PAGE_TITLE)
st.caption("Controle e análise da performance da conferência de recebimento.")

with st.expander("Sobre esta aplicação"):
    st.write(
        """
        Esta aplicação permite importar arquivos CSV ou Excel com dados de conferência,
        calcular indicadores operacionais, gerar ranking dos conferentes, analisar fornecedores
        e identificar alertas de produtividade e divergências.
        """
    )

    st.write("Colunas obrigatórias esperadas:")

    st.code(", ".join(COLUNAS_OBRIGATORIAS))


# ============================================================
# SIDEBAR - ENTRADA DE DADOS
# ============================================================

st.sidebar.title("Configurações")

modo_dados = st.sidebar.radio(
    "Fonte dos dados",
    options=[
        "Usar base de exemplo",
        "Importar arquivo CSV/Excel",
    ],
)

arquivo = None

if modo_dados == "Importar arquivo CSV/Excel":
    arquivo = st.sidebar.file_uploader(
        "Enviar arquivo",
        type=["csv", "xlsx"],
    )


# ============================================================
# CARREGAMENTO DOS DADOS
# ============================================================

try:
    if modo_dados == "Usar base de exemplo":
        df_original = gerar_base_exemplo()
    else:
        if arquivo is None:
            st.info("Envie um arquivo CSV ou Excel para iniciar a análise.")
            st.stop()

        df_original = carregar_arquivo(arquivo)

except Exception as erro:
    st.error("Erro ao carregar o arquivo.")
    st.exception(erro)
    st.stop()


# ============================================================
# VALIDAÇÃO DAS COLUNAS
# ============================================================

valido, colunas_faltantes = validar_colunas(df_original)

if not valido:
    st.error("O arquivo importado não possui todas as colunas obrigatórias.")

    st.write("Colunas faltantes:")

    for coluna in colunas_faltantes:
        st.write(f"- {coluna}")

    st.write("Colunas esperadas:")
    st.code(", ".join(COLUNAS_OBRIGATORIAS))

    st.write("Colunas encontradas no arquivo:")
    st.code(", ".join(df_original.columns))

    st.stop()


# ============================================================
# TRATAMENTO DOS DADOS
# ============================================================

df = tratar_dados(df_original)

if df.empty:
    st.warning("Após o tratamento, não restaram registros válidos para análise.")
    st.stop()


# ============================================================
# SIDEBAR - PARÂMETROS E FILTROS
# ============================================================

st.sidebar.divider()
st.sidebar.subheader("Parâmetros de análise")

meta_volume_por_hora = st.sidebar.number_input(
    "Meta mínima de volume por hora",
    min_value=0.0,
    value=150.0,
    step=10.0,
)

meta_divergencias_por_conferencia = st.sidebar.number_input(
    "Máximo de divergências por conferência",
    min_value=0.0,
    value=2.0,
    step=0.5,
)

st.sidebar.divider()
st.sidebar.subheader("Filtros")

data_min = df["data"].min().date()
data_max = df["data"].max().date()

periodo = st.sidebar.date_input(
    "Período",
    value=(data_min, data_max),
    min_value=data_min,
    max_value=data_max,
)

lista_fornecedores = sorted(df["fornecedor"].dropna().unique())
lista_tipos = sorted(df["tipo_mercadoria"].dropna().unique())
lista_conferentes = sorted(df["conferente"].dropna().unique())

fornecedores_selecionados = st.sidebar.multiselect(
    "Fornecedor",
    options=lista_fornecedores,
    default=lista_fornecedores,
)

tipos_selecionados = st.sidebar.multiselect(
    "Tipo de mercadoria",
    options=lista_tipos,
    default=lista_tipos,
)

conferentes_selecionados = st.sidebar.multiselect(
    "Conferente",
    options=lista_conferentes,
    default=lista_conferentes,
)


# ============================================================
# APLICAÇÃO DOS FILTROS
# ============================================================

df_filtrado = aplicar_filtros(
    df=df,
    periodo=periodo,
    fornecedores_selecionados=fornecedores_selecionados,
    tipos_selecionados=tipos_selecionados,
    conferentes_selecionados=conferentes_selecionados,
)

if df_filtrado.empty:
    st.warning("Nenhum registro encontrado com os filtros selecionados.")
    st.stop()


# ============================================================
# CÁLCULOS PRINCIPAIS
# ============================================================

kpis = calcular_kpis(df_filtrado)
ranking = calcular_ranking_conferentes(df_filtrado)
fornecedores = calcular_fornecedores(df_filtrado)


# ============================================================
# INDICADORES GERAIS
# ============================================================

st.subheader("Indicadores Gerais")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Volume total conferido",
    formatar_inteiro(kpis["volume_total"]),
)

col2.metric(
    "Quantidade de conferências",
    formatar_inteiro(kpis["quantidade_conferencias"]),
)

col3.metric(
    "Tempo médio por conferência",
    f"{formatar_numero(kpis['tempo_medio'])} min",
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "Produtividade média",
    f"{formatar_numero(kpis['produtividade_media'])} vol/h",
)

col5.metric(
    "Total de divergências",
    formatar_inteiro(kpis["divergencias_total"]),
)

col6.metric(
    "Divergências por conferência",
    formatar_numero(kpis["taxa_divergencia"]),
)


# ============================================================
# ABAS DO DASHBOARD
# ============================================================

aba_geral, aba_conferentes, aba_fornecedores, aba_alertas, aba_dados, aba_exportacao = st.tabs(
    [
        "Visão Geral",
        "Conferentes",
        "Fornecedores",
        "Alertas",
        "Dados",
        "Exportação",
    ]
)


# ============================================================
# ABA 1 - VISÃO GERAL
# ============================================================

with aba_geral:
    st.subheader("Visão Geral da Operação")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            grafico_volume_por_dia(df_filtrado),
            use_container_width=True,
        )

    with col2:
        st.plotly_chart(
            grafico_conferencias_por_dia(df_filtrado),
            use_container_width=True,
        )

    col3, col4 = st.columns(2)

    with col3:
        st.plotly_chart(
            grafico_volume_por_tipo(df_filtrado),
            use_container_width=True,
        )

    with col4:
        st.plotly_chart(
            grafico_tempo_por_tipo(df_filtrado),
            use_container_width=True,
        )


# ============================================================
# ABA 2 - CONFERENTES
# ============================================================

with aba_conferentes:
    st.subheader("Análise dos Conferentes")

    st.write("Ranking calculado com base em produtividade e divergências.")

    st.dataframe(
        ranking,
        use_container_width=True,
        hide_index=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            grafico_ranking_volume_por_hora(ranking),
            use_container_width=True,
        )

    with col2:
        st.plotly_chart(
            grafico_divergencias_por_conferente(ranking),
            use_container_width=True,
        )

    st.subheader("Comparativo Volume x Tempo")

    st.plotly_chart(
        grafico_volume_tempo_conferente(ranking),
        use_container_width=True,
    )


# ============================================================
# ABA 3 - FORNECEDORES
# ============================================================

with aba_fornecedores:
    st.subheader("Análise por Fornecedor")

    st.dataframe(
        fornecedores,
        use_container_width=True,
        hide_index=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            grafico_volume_por_fornecedor(fornecedores),
            use_container_width=True,
        )

    with col2:
        st.plotly_chart(
            grafico_divergencias_por_fornecedor(fornecedores),
            use_container_width=True,
        )

    st.subheader("Fornecedores com Maior Risco Operacional")

    fornecedores_risco = fornecedores[
        fornecedores["divergencias_por_conferencia"]
        > meta_divergencias_por_conferencia
    ]

    if fornecedores_risco.empty:
        st.success("Nenhum fornecedor acima do limite de divergências definido.")
    else:
        st.warning("Fornecedores acima do limite de divergências por conferência.")
        st.dataframe(
            fornecedores_risco,
            use_container_width=True,
            hide_index=True,
        )


# ============================================================
# ABA 4 - ALERTAS
# ============================================================

with aba_alertas:
    st.subheader("Alertas Automáticos")

    alertas_encontrados = False

    st.write("Critérios atuais:")

    st.write(
        f"- Meta mínima de produtividade: "
        f"{formatar_numero(meta_volume_por_hora)} volumes por hora"
    )

    st.write(
        f"- Máximo de divergências por conferência: "
        f"{formatar_numero(meta_divergencias_por_conferencia)}"
    )

    st.divider()

    conferentes_abaixo_meta = ranking[
        ranking["volume_por_hora"] < meta_volume_por_hora
    ]

    if not conferentes_abaixo_meta.empty:
        alertas_encontrados = True

        st.warning("Conferentes abaixo da meta de produtividade.")

        st.dataframe(
            conferentes_abaixo_meta[
                [
                    "posicao",
                    "conferente",
                    "volume_total",
                    "quantidade_conferencias",
                    "volume_por_hora",
                    "divergencias_por_conferencia",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.success("Nenhum conferente abaixo da meta de produtividade.")

    st.divider()

    conferentes_com_divergencia_alta = ranking[
        ranking["divergencias_por_conferencia"]
        > meta_divergencias_por_conferencia
    ]

    if not conferentes_com_divergencia_alta.empty:
        alertas_encontrados = True

        st.warning("Conferentes acima do limite de divergências.")

        st.dataframe(
            conferentes_com_divergencia_alta[
                [
                    "posicao",
                    "conferente",
                    "quantidade_conferencias",
                    "divergencias_total",
                    "divergencias_por_conferencia",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.success("Nenhum conferente acima do limite de divergências.")

    st.divider()

    fornecedores_com_divergencia_alta = fornecedores[
        fornecedores["divergencias_por_conferencia"]
        > meta_divergencias_por_conferencia
    ]

    if not fornecedores_com_divergencia_alta.empty:
        alertas_encontrados = True

        st.warning("Fornecedores acima do limite de divergências.")

        st.dataframe(
            fornecedores_com_divergencia_alta,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.success("Nenhum fornecedor acima do limite de divergências.")

    st.divider()

    if not alertas_encontrados:
        st.info("A operação está dentro dos parâmetros definidos.")


# ============================================================
# ABA 5 - DADOS
# ============================================================

with aba_dados:
    st.subheader("Dados Filtrados")

    st.write(f"Total de registros filtrados: {len(df_filtrado)}")

    st.dataframe(
        df_filtrado,
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Resumo Estatístico")

    st.dataframe(
        df_filtrado[
            [
                "volume_conferido",
                "tempo_minutos",
                "divergencias",
                "volume_por_hora",
            ]
        ].describe(),
        use_container_width=True,
    )


# ============================================================
# ABA 6 - EXPORTAÇÃO
# ============================================================

with aba_exportacao:
    st.subheader("Exportação de Relatórios")

    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")

    csv_filtrado = df_filtrado.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Baixar dados filtrados em CSV",
        data=csv_filtrado,
        file_name=f"dados_filtrados_{data_hora}.csv",
        mime="text/csv",
    )

    excel_relatorio = converter_df_para_excel(
        {
            "Dados Filtrados": df_filtrado,
            "Ranking Conferentes": ranking,
            "Fornecedores": fornecedores,
        }
    )

    st.download_button(
        label="Baixar relatório completo em Excel",
        data=excel_relatorio,
        file_name=f"relatorio_conferencia_{data_hora}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    st.info(
        """
        O arquivo Excel exportado contém:

        - dados filtrados;
        - ranking dos conferentes;
        - análise por fornecedor.
        """
    )


# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.caption(
    "Dashboard desenvolvido em Python + Streamlit para análise de conferência de mercadorias."
)