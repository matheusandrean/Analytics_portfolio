# 📊 Credit Risk Analysis: German Credit Data

## 📋 Sobre o Projeto
Este projeto utiliza dados do **Statlog (German Credit Data)** para prever a probabilidade de inadimplência de clientes, aplicando técnicas de **Machine Learning**. A análise combina exploração de dados, engenharia de variáveis e modelagem preditiva para oferecer insights valiosos para gestão de crédito.

O objetivo principal é construir um pipeline completo, desde a exploração inicial dos dados até a avaliação detalhada do desempenho do modelo, destacando o impacto das variáveis no risco de crédito.

---

## 🚀 Objetivos
- Desenvolver e avaliar um modelo de **Regressão Logística** para prever o risco de crédito.
- Identificar os fatores mais relevantes para inadimplência.
- Aplicar técnicas de pré-processamento e balanceamento de classes para melhorar a qualidade dos dados.
- Visualizar as tendências e padrões nos dados de crédito.

---

## 🛠️ Tecnologias e Ferramentas
- **Python**: Para manipulação de dados e modelagem.
- **Bibliotecas**:
  - `pandas`, `numpy`: Limpeza e manipulação de dados.
  - `matplotlib`, `seaborn`: Criação de visualizações.
  - `scikit-learn`: Construção e avaliação do modelo preditivo.

---

## 📊 Etapas do Projeto
1. **Exploração de Dados**:
   - Carregamento do conjunto de dados diretamente do repositório [Statlog (German Credit Data)](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)).
   - Análise exploratória para identificar padrões e inconsistências.
   - Visualização da distribuição das variáveis e matriz de correlação.

2. **Pré-Processamento**:
   - Codificação de variáveis categóricas com `get_dummies`.
   - Normalização das variáveis numéricas com `StandardScaler`.
   - Separação dos dados em conjuntos de treino (70%) e teste (30%).

3. **Modelagem**:
   - Treinamento de um modelo de **Regressão Logística** para previsão binária.
   - Geração de probabilidades para avaliação da curva ROC.

4. **Avaliação**:
   - Métricas de avaliação: `Accuracy`, `Precision`, `Recall`, `F1-Score`, `AUC-ROC`.
   - Matriz de confusão e curva ROC para análise de desempenho.

---

## 🔑 Principais Resultados
### Métricas do Modelo
- **Acurácia**: 76%
- **AUC-ROC**: 0.81
- **Precisão (Class 1 - Risco)**: 74%
- **Recall (Class 1 - Risco)**: 71%

### Insights
- **Variáveis com maior impacto**:
  - **Credit_amount**: Clientes com maior valor de crédito são mais propensos a inadimplência.
  - **Duration_in_month**: Aumento na duração do crédito eleva o risco.
  - **Age_in_years**: Clientes mais jovens demonstram maior risco.

### Visualizações
- **Distribuição da Variável Alvo**:
  ![Distribuição da Variável Alvo](#)
- **Matriz de Correlação**:
  ![Matriz de Correlação](#)
- **Curva ROC**:
  ![Curva ROC](#)

---

## 📂 Estrutura do Projeto
```plaintext
.
├── data/
│   ├── raw/                  # Dados originais
│   ├── processed/            # Dados tratados
├── notebooks/
│   ├── credit_risk_analysis.ipynb  # Análise completa do projeto
├── reports/
│   ├── figures/              # Gráficos e visualizações
├── README.md                 # Documentação do projeto
