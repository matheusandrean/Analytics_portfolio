<!-- README (HTML) — Credit Risk Scoring · End-to-End (Portfolio Case) -->
<h1 align="left">Credit Risk Scoring · End-to-End (Portfolio Case)</h1>

<p>
  <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white"></a>
  <a href="#"><img alt="FastAPI" src="https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white"></a>
  <a href="#"><img alt="License" src="https://img.shields.io/badge/License-MIT-black"></a>
</p>

<p>
Projeto completo de <strong>Análise de Risco de Crédito</strong> usando o dataset público <em>UCI Credit Card</em>.
Entrega: <strong>EDA</strong>, <strong>modelagem</strong> (Logistic, Tree, Random Forest, <strong>XGBoost</strong>), 
tratamento de desbalanceamento, <strong>explicabilidade (SHAP)</strong>, export para dashboard e 
<strong>API de scoring (FastAPI)</strong> para simular aprovação/recusa com política de decisão configurável.
</p>

<blockquote>
  <strong>Objetivo:</strong> estimar a <em>Probability of Default (PD)</em> para apoiar a decisão de crédito 
  (<code>approve</code> / <code>approve_with_low_limit</code> / <code>review</code> / <code>deny</code>) com transparência e reprodutibilidade.
</blockquote>

<hr/>

<h2>🚀 Como rodar (rápido)</h2>

<h3>1) Notebook no Google Colab</h3>
<p>Abra e execute o notebook (gera CSVs para BI em <code>dashboards/export/</code>):</p>
<pre><code>notebooks/Credit_Scoring_EndToEnd.ipynb
</code></pre>

<h3>2) Ambiente local (Windows / Linux / macOS)</h3>
<pre><code># criar e ativar o ambiente
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
# source .venv/bin/activate

# instalar dependências
pip install -r requirements.txt

# treinar e exportar artefatos de produção
python scripts/train_export.py
</code></pre>

<p>Saídas em <code>models/</code>:</p>
<ul>
  <li><code>preprocess.pkl</code> — pipeline de pré-processamento</li>
  <li><code>model_xgb.pkl</code> — classificador final</li>
  <li><code>metadata.json</code> — ordem de features, métricas e metadados</li>
  <li><code>thresholds.json</code> — política de decisão (approve/review/deny)</li>
</ul>

<h3>3) API de Scoring (FastAPI)</h3>
<pre><code># iniciar serviço
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
</code></pre>
<ul>
  <li>Healthcheck: <code>http://localhost:8000/health</code></li>
  <li>Docs (Swagger): <code>http://localhost:8000/docs</code></li>
</ul>
<p>
Para testar <code>POST /score</code>, envie um JSON com as <strong>mesmas features</strong> listadas em 
<code>models/metadata.json</code> → <code>feature_order</code>.
</p>

<hr/>

<h2>📦 Estrutura do projeto</h2>
<pre><code>.
├─ notebooks/                 # EDA, modelagem, SHAP, export p/ dashboard
├─ src/                       # utils + pipeline de pré-processamento
├─ scripts/                   # treino/export e runner da API
├─ api/                       # FastAPI (endpoints /health /score)
├─ dashboards/export/         # CSVs (Looker Studio / Power BI)
├─ models/                    # artefatos de produção (.pkl / .json)
├─ data/                      # dataset (baixado pelo notebook/script)
├─ assets/                    # imagens (opcional p/ README)
├─ requirements.txt
├─ example_request.json
├─ LICENSE
└─ README.md
</code></pre>

<hr/>

<h2>🧠 O que está implementado</h2>
<ul>
  <li><strong>Modelos:</strong> Regressão Logística, Decision Tree, Random Forest, <strong>XGBoost</strong> (selecionado).</li>
  <li><strong>Validação:</strong> holdout + métricas <strong>AUC</strong>, <strong>F1</strong>, <strong>Recall</strong>, <strong>Precision</strong>.</li>
  <li><strong>Desbalanceamento:</strong> <code>RandomOverSampler</code> <em>apenas no treino</em>.</li>
  <li><strong>Explicabilidade:</strong> <strong>SHAP</strong> (top razões por cliente no endpoint <code>/score</code>).</li>
  <li><strong>Política de decisão:</strong> thresholds configuráveis em <code>models/thresholds.json</code>.</li>
</ul>

<hr/>

<h2>📊 Dashboard</h2>
<p>
Conecte os CSVs de <code>dashboards/export/</code> no <strong>Looker Studio</strong> (via Google Sheets) 
ou no <strong>Power BI</strong> (Get Data → Text/CSV). Sugestões de visuais: 
KPIs (AUC, F1, Recall), curva ROC, distribuição de <code>score_proba</code> × <code>y_true</code>, 
barras de importância de features.
</p>

<hr/>

<h2>🛠️ Dicas &amp; Troubleshooting</h2>
<ul>
  <li><strong>Erro de features no /score:</strong> confira <code>models/metadata.json</code> → <code>feature_order</code> e envie <em>todas</em> as colunas com valores numéricos.</li>
  <li><strong>SHAP lento:</strong> use amostras menores para explicações (ajustável no notebook e na API).</li>
  <li><strong>Oversampling em produção?</strong> Nunca — apenas no treino. Em runtime: <code>preprocess.pkl</code> → <code>model_xgb.pkl</code> → <code>predict_proba</code>.</li>
</ul>

<hr/>

<h2>🧭 Roadmap</h2>
<ul>
  <li>Deploy da API com Docker (Render/Fly.io/AWS).</li>
  <li>Monitoramento de <em>data drift</em> e re-treino programado.</li>
  <li>Auditoria de <em>fairness</em> e scorecards regulatórios (KS/deciles).</li>
  <li>Integração com bureaus e variáveis macroeconômicas.</li>
  <li>CI simples (GitHub Actions) + testes do pipeline.</li>
</ul>

<hr/>

<h2>📝 Licença</h2>
<p>Distribuído sob a <strong>MIT License</strong>.</p>

<p><em>Este case foi desenvolvido para demonstrar minhas habilidades em Ciência de Dados aplicada a Finanças:
modelagem tabular, boas práticas de engenharia de dados, explicabilidade e entrega ponta a ponta.</em></p>
