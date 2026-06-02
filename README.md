# Dashboard de Conferência de Mercadorias

Aplicação desenvolvida em Python com Streamlit para controle e análise da performance da conferência de mercadorias.

## Objetivo

Automatizar a análise de dados exportados em CSV ou Excel, permitindo visualizar indicadores operacionais, ranking de conferentes, divergências, produtividade e alertas.

## Funcionalidades

- Upload de arquivos CSV ou Excel
- Validação automática das colunas obrigatórias
- Tratamento dos dados
- Filtros por período, fornecedor, tipo de mercadoria e conferente
- Indicadores gerais
- Ranking de conferentes
- Análise por fornecedor
- Gráficos interativos
- Alertas automáticos
- Exportação em CSV
- Exportação em Excel

## Colunas obrigatórias

O arquivo importado deve conter as seguintes colunas:

```text
data
conferencia_id
fornecedor
tipo_mercadoria
conferente
volume_conferido
tempo_minutos
divergencias