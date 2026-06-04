# Dashboard de Conferência de Mercadorias

🌐 Idioma: Português | [English](README.md)


Aplicação desenvolvida em **Python** e **Streamlit** para automatizar o controle, a análise e o acompanhamento da performance da conferência de mercadorias.

O dashboard transforma arquivos operacionais em informações claras para apoiar decisões, identificar gargalos, acompanhar a produtividade da equipe e reduzir o tempo gasto com análises manuais em planilhas.

## Visão geral

Empresas que realizam recebimento e conferência de mercadorias precisam acompanhar indicadores como volume conferido, tempo de operação, divergências encontradas e produtividade dos conferentes.

Quando essas análises são feitas manualmente, o processo pode consumir tempo, gerar retrabalho e dificultar a identificação de problemas operacionais.

Este projeto centraliza essas informações em um dashboard interativo, permitindo que gestores acompanhem os principais indicadores da operação de forma rápida e visual.

## Demonstração

Adicione nesta seção uma imagem ou animação do dashboard em funcionamento.

```markdown
![Dashboard de Conferência de Mercadorias](docs/images/dashboard.png)
```

## Principais benefícios

- Redução do tempo gasto na análise manual de planilhas
- Centralização dos indicadores de conferência
- Identificação de gargalos e perdas de produtividade
- Acompanhamento da performance individual dos conferentes
- Identificação de fornecedores com maior índice de divergências
- Apoio à tomada de decisão com dados atualizados
- Exportação dos resultados para compartilhamento e análise adicional

## Funcionalidades

- Upload de arquivos nos formatos CSV ou Excel
- Validação automática das colunas obrigatórias
- Tratamento e padronização dos dados importados
- Filtros por período, fornecedor, tipo de mercadoria e conferente
- Indicadores gerais da operação
- Ranking de produtividade dos conferentes
- Análise de performance por fornecedor
- Análise de divergências
- Gráficos interativos
- Alertas automáticos para situações que exigem atenção
- Exportação dos dados filtrados em CSV
- Exportação dos resultados em Excel

## Indicadores disponíveis

O dashboard permite acompanhar indicadores como:

- Volume total de mercadorias conferidas
- Quantidade de conferências realizadas
- Tempo médio por conferência
- Volume médio conferido por operação
- Produtividade por conferente
- Quantidade total de divergências
- Taxa de divergências por fornecedor
- Ranking de conferentes
- Fornecedores com maior incidência de problemas

## Filtros de análise

Os dados podem ser analisados de forma dinâmica utilizando filtros por:

- Período
- Fornecedor
- Tipo de mercadoria
- Conferente

Os indicadores, tabelas e gráficos são atualizados automaticamente de acordo com os filtros selecionados.

## Estrutura esperada do arquivo

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
```

## Exemplo de dados

| data | conferencia_id | fornecedor | tipo_mercadoria | conferente | volume_conferido | tempo_minutos | divergencias |
|---|---:|---|---|---|---:|---:|---:|
| 2026-05-01 | 1001 | Fornecedor A | Alimentos | João | 450 | 35 | 2 |
| 2026-05-01 | 1002 | Fornecedor B | Bebidas | Maria | 620 | 42 | 0 |
| 2026-05-02 | 1003 | Fornecedor A | Limpeza | Carlos | 380 | 31 | 4 |

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL

## Como executar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_PROJETO
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no macOS ou Linux:

```bash
source .venv/bin/activate
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run app.py
```

Após a execução, o dashboard será aberto no navegador.

## Possibilidades de personalização

A solução pode ser adaptada para diferentes necessidades operacionais, incluindo:

- Integração com arquivos exportados de sistemas ERP
- Inclusão de novos indicadores de desempenho
- Criação de metas por conferente ou equipe
- Envio automático de relatórios
- Integração com banco de dados
- Controle de acesso por usuário
- Publicação em ambiente web ou nuvem
- Personalização da identidade visual da empresa

## Aplicações possíveis

Este dashboard pode ser utilizado por empresas que trabalham com:

- Recebimento de mercadorias
- Centros de distribuição
- Supermercados
- Atacadistas
- Operações logísticas
- Controle de estoque
- Auditoria de fornecedores

## Objetivo do projeto

Este projeto foi desenvolvido para demonstrar como Python e Streamlit podem ser utilizados para transformar dados operacionais em uma ferramenta de gestão simples, visual e eficiente.

A solução é especialmente útil para empresas que ainda dependem de planilhas manuais e desejam melhorar o controle, a produtividade e a qualidade das suas operações.

## Autor

**Jorge Krummenauer**

Engenharia, gestão industrial e desenvolvimento de software aplicados à melhoria de processos, redução de custos e tomada de decisão.