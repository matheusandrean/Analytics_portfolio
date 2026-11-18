![Analytics Portfolio](assets/banner.svg)

# Analytics Portfolio

**Matheus Marcondes · Cofundador da GovernandoAI**

Repositório central dos meus projetos em **Data Science, GenAI Engineering, Machine Learning, Data Governance e Financial Intelligence**. Reúne plataformas de crédito, estudos analíticos e a evolução planejada do Sentinel by GovernandoAI, com código, dados demonstrativos, documentação e critérios de avaliação no mesmo lugar.

[LinkedIn](https://www.linkedin.com/in/matmarcondes/) · [Perfil GitHub](https://github.com/matheusandrean) · [Documentação original](docs/README.legacy.md)

## Explore os projetos

| Projeto | Pergunta e escopo | Evidências disponíveis |
| --- | --- | --- |
| [Credit Intelligence AI](projects/credit-intelligence-ai/) | Plataforma de apoio à análise de crédito com ML, SHAP, GenAI, RAG, FastAPI e Streamlit | [Guia](projects/credit-intelligence-ai/README.pt-BR.md), [arquitetura](projects/credit-intelligence-ai/ARCHITECTURE.md), [governança](projects/credit-intelligence-ai/GOVERNANCE.pt-BR.md) |
| [Credit Risk Intelligence Web](projects/credit-risk-intelligence-web/) | Dashboard estático de carteira, originação, risco e cobrança com dados sintéticos | [Guia e metodologia](projects/credit-risk-intelligence-web/README.md), [código](projects/credit-risk-intelligence-web/app.js), [agregados](projects/credit-risk-intelligence-web/assets/portfolio-data.json) |
| [Risco de crédito · End-to-End](ML/risco_de_credito/) | Estudo de scoring, pipeline e disponibilização por API | [Documentação](ML/risco_de_credito/README.md), [treinamento](ML/risco_de_credito/scripts/train_export.py), [API](ML/risco_de_credito/api/main.py) |
| [Credit Risk Analysis](ML/credit_risk_analysis/) | Estudo de classificação de risco de crédito | [Documentação](ML/credit_risk_analysis/README.md), [notebook](ML/credit_risk_analysis/Analise_de_credito/credit_risk_analysis.ipynb) |
| [Análise de churn](ML/Analise_Churn/) | Exploração de cancelamento de clientes de telecomunicações | [Documentação](ML/Analise_Churn/README.md), [notebook](ML/Analise_Churn/Analise_de_Churn_o_Telco_Portfolio.ipynb) |
| [Food Order Prediction](ML/FoodOrderPrediction/) | Estudo de recompra em serviços de alimentação | [Notebook](ML/FoodOrderPrediction/FoodOrderPrediction.ipynb), [contexto e fonte original](ML/FoodOrderPrediction/readme.txt) |
| [Automação de relatórios](ML/Auto_email/) | Extração, geração de relatório e envio de e-mail | [Documentação](ML/Auto_email/README.md), [implementação](ML/Auto_email/main.py) |

## Organização

```text
Analytics_portfolio/
├── projects/
│   ├── credit-intelligence-ai/        # Python, modelos, API, Streamlit e testes
│   └── credit-risk-intelligence-web/  # HTML, CSS, JavaScript e dados sintéticos
├── ML/                               # Estudos e aplicações existentes
├── profile/                          # Fonte do README especial do perfil
├── docs/                             # Identidade, migração e documentação histórica
└── .github/workflows/                # CI dos projetos no repositório central
```

[Detalhes da consolidação e origem dos arquivos](docs/CONSOLIDATION.md).

## Como avaliar e reproduzir

Clone o portfólio uma única vez:

```bash
git clone https://github.com/matheusandrean/Analytics_portfolio.git
cd Analytics_portfolio
```

Para a plataforma Python, entre em `projects/credit-intelligence-ai` e siga o [guia de execução](projects/credit-intelligence-ai/README.pt-BR.md#como-executar). Para o dashboard, execute a partir da raiz:

```bash
python -m http.server 8000 --directory projects/credit-risk-intelligence-web
```

Acesse `http://localhost:8000`. A publicação central no GitHub Pages ainda não foi configurada.

Cada pasta tem contexto e dependências próprios. Comece pela documentação do projeto, examine os dados e execute o notebook ou script em um ambiente virtual separado. Não há um ambiente único nem uma suíte de testes que certifique todos os estudos deste repositório.

Para o estudo de crédito com API, siga a preparação dos dados, o treinamento e a exportação de artefatos descritos no [guia específico](ML/risco_de_credito/README.md). Para automação de e-mails, revise as configurações e use um ambiente de teste antes de executar rotinas que enviam mensagens.

## Resultados e limites

As análises, saídas de notebooks e documentação técnica foram preservadas. As métricas do README anterior estão no [registro original](docs/README.legacy.md); não foram reexecutadas nesta reformulação e não devem ser interpretadas como desempenho atual validado. Benefícios de negócio apresentados nos estudos são hipóteses de aplicação, sem medição de impacto operacional neste portfólio.

Os estudos usam conjuntos de dados e metodologias distintos. A documentação de cada projeto é a referência para sua origem; este repositório não adota uma declaração única de dados sintéticos. Antes de comparar resultados, verifique divisão de dados, target, pré-processamento e protocolo de avaliação.

## Sentinel by GovernandoAI

A próxima fase será desenvolvida em `projects/sentinel/`, neste mesmo repositório. O escopo planejado integra Python, XGBoost, Isolation Forest, SHAP, qualidade e governança de dados, contratos, linhagem, auditoria, drift, FastAPI, Streamlit, testes e CI/CD. Usará dados sintéticos, validação temporal e métricas verificáveis; RAG, AML e GenAI fazem parte da evolução prevista.

**Status: planejado.** A implementação antifraude e seus resultados ainda não foram produzidos. A pasta será criada quando o desenvolvimento começar.

## Perfil e identidade

O conteúdo do perfil é mantido em [profile/README.md](profile/README.md). O GitHub exige uma cópia no repositório especial `matheusandrean/matheusandrean` para exibi-lo na página do usuário; essa é a única exceção à centralização.

A [identidade visual provisória](docs/VISUAL_IDENTITY.md) usa azul-marinho e ciano, até confirmação das cores oficiais da GovernandoAI.
