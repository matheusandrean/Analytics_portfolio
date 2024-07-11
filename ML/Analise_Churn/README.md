
# Análise de Churn da Telco

Este projeto faz parte do meu portfólio de Análise de BI, focado na análise de churn em uma empresa de telecomunicações. O objetivo é explorar os dados, identificar padrões e construir um modelo preditivo para prever o cancelamento de serviços pelos clientes.

## Sumário

1. [Introdução](#introdução)
2. [Exploração de Dados](#exploração-de-dados)
3. [Análise de Distribuição](#análise-de-distribuição)
4. [Análise de Correlações](#análise-de-correlações)
5. [Modelagem Preditiva](#modelagem-preditiva)
6. [Visualizações Adicionais](#visualizações-adicionais)
7. [Conclusão](#conclusão)

## Introdução

Neste projeto, analisamos dados de uma empresa de telecomunicações para entender os fatores que contribuem para o churn (cancelamento) dos clientes. Utilizamos técnicas de análise exploratória de dados (EDA) e modelagem preditiva para identificar padrões e prever cancelamentos futuros.

## Exploração de Dados

A análise começa com o carregamento e a visualização inicial dos dados. Utilizamos bibliotecas como `pandas` e `matplotlib` para manipulação e visualização dos dados. Exploramos as principais características do dataset, como distribuição de variáveis e valores ausentes.

## Análise de Distribuição

Analisamos a distribuição do churn no dataset para entender a proporção de clientes que cancelaram o serviço em relação aos que permaneceram. Esta etapa é crucial para identificar desequilíbrios nos dados que podem impactar a modelagem preditiva.

## Análise de Correlações

Exploramos as correlações entre o churn e outras variáveis categóricas relevantes, como tipo de contrato, serviços adicionais, e suporte ao cliente. Utilizamos visualizações como gráficos de barras e heatmaps para identificar relações significativas.

## Modelagem Preditiva

Construímos um modelo de regressão logística para prever o churn dos clientes. A modelagem incluiu:

- Preparação dos dados: Tratamento de variáveis categóricas e normalização.
- Divisão dos dados: Separação em conjuntos de treino e teste.
- Treinamento do modelo: Ajuste e validação do modelo de regressão logística.
- Avaliação do modelo: Medição da performance utilizando métricas como acurácia, precisão, recall e a matriz de confusão.

## Visualizações Adicionais

Adicionamos visualizações para uma compreensão mais profunda dos resultados do modelo, incluindo a matriz de confusão e a importância das características do modelo preditivo. Estas visualizações ajudam a identificar quais características têm maior impacto na previsão de churn.

## Conclusão

Esta análise cobriu:

1. **Exploração de Dados**: Carregamento e visualização inicial dos dados.
2. **Análise de Distribuição**: Distribuição de cancelamento no dataset.
3. **Análise de Correlações**: Relações entre cancelamento e variáveis categóricas relevantes.
4. **Modelagem Preditiva**: Construção e avaliação de um modelo de regressão logística para prever cancelamento.
5. **Visualizações Adicionais**: Matriz de confusão e importância das características.

Este projeto demonstra minhas habilidades em análise de dados, visualização e modelagem preditiva aplicadas a um problema de negócio real.

---

Para mais detalhes, confira o notebook completo no repositório.
