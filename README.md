![Analytics Portfolio](assets/banner.svg)

# Analytics Portfolio

**Matheus Marcondes · Cofundador da GovernandoAI**

Estudos e aplicações de Data Science e Machine Learning, com foco em perguntas de negócio, análise de dados e comunicação dos limites dos modelos. Meu posicionamento conecta essas bases a GenAI Engineering, Data Governance e Financial Intelligence.

[LinkedIn](https://www.linkedin.com/in/matmarcondes/) · [Perfil GitHub](https://github.com/matheusandrean) · [Documentação original](docs/README.legacy.md)

## Explore os projetos

| Projeto | Pergunta e escopo | Evidências disponíveis |
| --- | --- | --- |
| [Risco de crédito · End-to-End](ML/risco_de_credito/) | Estudo de scoring, pipeline e disponibilização por API | [Documentação](ML/risco_de_credito/README.md), [treinamento](ML/risco_de_credito/scripts/train_export.py), [API](ML/risco_de_credito/api/main.py) |
| [Credit Risk Analysis](ML/credit_risk_analysis/) | Estudo de classificação de risco de crédito | [Documentação](ML/credit_risk_analysis/README.md), [notebook](ML/credit_risk_analysis/Analise_de_credito/credit_risk_analysis.ipynb) |
| [Análise de churn](ML/Analise_Churn/) | Exploração de cancelamento de clientes de telecomunicações | [Documentação](ML/Analise_Churn/README.md), [notebook](ML/Analise_Churn/Analise_de_Churn_o_Telco_Portfolio.ipynb) |
| [Food Order Prediction](ML/FoodOrderPrediction/) | Estudo de recompra em serviços de alimentação | [Notebook](ML/FoodOrderPrediction/FoodOrderPrediction.ipynb), [contexto e fonte original](ML/FoodOrderPrediction/readme.txt) |
| [Automação de relatórios](ML/Auto_email/) | Extração, geração de relatório e envio de e-mail | [Documentação](ML/Auto_email/README.md), [implementação](ML/Auto_email/main.py) |

## Como avaliar e reproduzir

Cada pasta tem contexto e dependências próprios. Comece pela documentação do projeto, examine os dados e execute o notebook ou script em um ambiente virtual separado. Não há um ambiente único nem uma suíte de testes que certifique todos os estudos deste repositório.

Para o estudo de crédito com API, siga a preparação dos dados, o treinamento e a exportação de artefatos descritos no [guia específico](ML/risco_de_credito/README.md). Para automação de e-mails, revise as configurações e use um ambiente de teste antes de executar rotinas que enviam mensagens.

## Resultados e limites

As análises, saídas de notebooks e documentação técnica foram preservadas. As métricas do README anterior estão no [registro original](docs/README.legacy.md); não foram reexecutadas nesta reformulação e não devem ser interpretadas como desempenho atual validado. Benefícios de negócio apresentados nos estudos são hipóteses de aplicação, sem medição de impacto operacional neste portfólio.

Os estudos usam conjuntos de dados e metodologias distintos. A documentação de cada projeto é a referência para sua origem; este repositório não adota uma declaração única de dados sintéticos. Antes de comparar resultados, verifique divisão de dados, target, pré-processamento e protocolo de avaliação.

## Financial Intelligence e GenAI

- [Credit Intelligence AI](https://github.com/matheusandrean/credit-intelligence-ai): plataforma de apoio à análise de crédito com modelos quantitativos, explicabilidade, GenAI e documentação de governança.
- [Credit Risk Intelligence Web](https://github.com/matheusandrean/credit-risk-intelligence-web): case interativo de carteira, originação, risco e cobrança com dados sintéticos.

A [identidade visual provisória](docs/VISUAL_IDENTITY.md) usa azul-marinho e ciano, até confirmação das cores oficiais da GovernandoAI.
