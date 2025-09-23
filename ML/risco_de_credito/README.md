<!-- README (HTML) — Credit Risk Scoring · End-to-End -->
<h1 align="left">Credit Risk Scoring · End-to-End</h1>

<p>
  <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white"></a>
  <a href="#"><img alt="FastAPI" src="https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white"></a>
  <a href="#"><img alt="XGBoost" src="https://img.shields.io/badge/Model-XGBoost-EB5F07"></a>
  <a href="#"><img alt="License" src="https://img.shields.io/badge/License-MIT-black"></a>
</p>

<p>
Este é um case completo de <strong>Análise de Risco de Crédito</strong> usando o dataset público
<em>UCI Credit Card</em>. O objetivo é demonstrar, de ponta a ponta, como eu estruturaria um
score de crédito: da EDA e modelagem até uma API de scoring (em FastAPI) que retorna a
<strong>Probability of Default (PD)</strong>, aplica uma <strong>política de decisão</strong> (approve / approve_with_low_limit / review / deny) e fornece
<strong>explicabilidade</strong> com SHAP.
</p>

<hr/>

<h2>🔍 Intuição do Projeto</h2>
<p>
Quando um cliente pede cartão, empréstimo ou financiamento, a instituição precisa responder em segundos:
</p>
<ul>
  <li>Qual a probabilidade desse cliente <strong>não pagar</strong> (PD)?</li>
  <li>Devo aprovar, revisar ou negar?</li>
  <li>Se aprovar, qual limite faz sentido para o risco?</li>
</ul>
<p>
Aqui eu simulo esse fluxo com dados públicos: gero a PD por cliente, aplico thresholds configuráveis para a decisão
e devolvo explicações locais (SHAP) para cada predição — o que ajuda produto, risco e compliance.
</p>

<hr/>

<h2>🚀 O que foi feito</h2>
<ul>
  <li><strong>EDA</strong>: análise exploratória, distribuição do target e correlações.</li>
  <li><strong>Modelagem</strong>: Logistic Regression, Decision Tree, Random Forest e <strong>XGBoost</strong>.</li>
  <li><strong>Desbalanceamento</strong>: <code>RandomOverSampler</code> (apenas no treino).</li>
  <li><strong>Métricas</strong>: AUC, F1, Recall, Precision + curva ROC.</li>
  <li><strong>Explicabilidade</strong>: SHAP (top razões por cliente).</li>
  <li><strong>Export</strong>: CSVs para dashboards (Looker Studio / Power BI).</li>
  <li><strong>API</strong>: FastAPI com endpoints <code>/health</code>, <code>/docs</code> e <code>/score</code>.</li>
</ul>

<hr/>

<h2>📦 Estrutura</h2>
<pre><code>.
├─ notebooks/            # EDA, modelagem, SHAP, export
├─ src/                  # utils e pipeline (pré-processamento)
├─ scripts/              # treino/export e runner da API
├─ api/                  # FastAPI (score, health, docs)
├─ dashboards/export/    # CSVs para BI
├─ models/               # artifacts: preprocess.pkl, model_xgb.pkl, *.json
├─ data/                 # dataset (baixado no notebook/script)
├─ example_request.json  # exemplo de payload para POST /score
├─ requirements.txt
└─ README.md
</code></pre>

<hr/>

<h2>⚙️ Como rodar</h2>

<h3>1) Notebook no Google Colab</h3>
<p>Execute o notebook principal (gera CSVs para BI em <code>dashboards/export/</code>):</p>
<pre><code>notebooks/Credit_Scoring_EndToEnd.ipynb
</code></pre>

<h3>2) Ambiente local (Windows / Linux / macOS)</h3>
<pre><code># criar e ativar o ambiente
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
# source .venv/bin/activate

# dependências
pip install -r requirements.txt

# treinar e exportar artefatos de produção
python scripts/train_export.py
</code></pre>

<p>Saídas em <code>models/</code>:</p>
<ul>
  <li><code>preprocess.pkl</code> — pipeline de pré-processamento (imputer + scaler)</li>
  <li><code>model_xgb.pkl</code> — classificador final</li>
  <li><code>metadata.json</code> — ordem de features, métricas e metadados</li>
  <li><code>thresholds.json</code> — política de decisão (approve / review / deny)</li>
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
Para testar <code>POST /score</code>, envie um JSON com as <strong>mesmas features</strong> em
<code>models/metadata.json</code> → <code>feature_order</code>.
</p>

<hr/>

<h2>🧠 Modelo e política de decisão</h2>
<ul>
  <li><strong>Modelos avaliados</strong>: Logistic, Tree, RandomForest e XGBoost (selecionado).</li>
  <li><strong>Validação</strong>: holdout em teste; métricas AUC/F1/Recall/Precision.</li>
  <li><strong>Desbalanceamento</strong>: oversampling só no treino (nunca na inferência).</li>
  <li><strong>Política</strong>: thresholds calibrados a partir do melhor F1 e ajustados. Em resumo:
    <ul>
      <li>PD ≤ <code>approve_threshold</code> → <strong>APPROVE</strong></li>
      <li><code>approve</code> &lt; PD ≤ <code>review_threshold</code> → <strong>APPROVE_WITH_LOW_LIMIT</strong></li>
      <li><code>review</code> &lt; PD ≤ <code>deny_threshold</code> → <strong>REVIEW</strong></li>
      <li>PD &gt; <code>deny_threshold</code> → <strong>DENY</strong></li>
    </ul>
  </li>
</ul>

<hr/>

<h2>📊 Dashboard</h2>
<p>Conecte os CSVs de <code>dashboards/export/</code> diretamente no:</p>
<ul>
  <li><strong>Looker Studio</strong> (via Google Sheets)</li>
  <li><strong>Power BI</strong> (Get Data → Text/CSV)</li>
</ul>
<p>Sugestões de visuais: KPIs (AUC, F1, Recall), curva ROC, distribuição de <code>score_proba</code> × <code>y_true</code>, barras de importância.</p>

<hr/>

<h2>🛠️ Dicas &amp; Troubleshooting</h2>
<ul>
  <li><strong>Erro de features no /score</strong>: confira <code>models/metadata.json</code> → <code>feature_order</code> e envie <em>todas</em> as colunas numéricas esperadas.</li>
  <li><strong>SHAP lento</strong>: use amostras menores (o notebook já trata isso em exemplo).</li>
  <li><strong>Oversampling em produção</strong>: nunca — só no treino. Em runtime: <code>preprocess.pkl</code> → <code>model_xgb.pkl</code> → <code>predict_proba</code>.</li>
</ul>

<hr/>

<h2>🧭 Próximos passos</h2>
<ul>
  <li>Containerizar a API (Docker) e publicar.</li>
  <li>Monitorar <em>data drift</em> e re-treino programado.</li>
  <li>Auditar fairness (aprovação por grupos) e scorecards (KS / deciles).</li>
  <li>Integrar variáveis externas (macro, bureaus) e feature store.</li>
  <li>CI/CD simples com GitHub Actions.</li>
</ul>

<hr/>

<h2>📝 Licença</h2>
<p>Distribuído sob a <strong>MIT License</strong>.</p>

<p><em>
Este case foi produzido para demonstrar habilidades práticas em Ciência de Dados aplicada a Finanças:
modelagem tabular, boas práticas de pipeline, explicabilidade e entrega operável via API.
</em></p>
