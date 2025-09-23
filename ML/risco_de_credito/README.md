# Credit Risk Scoring — End-to-End (Portfolio Case)

Projeto completo de **Análise de Risco de Crédito** com dados do UCI Credit Card: EDA, modelagem, explicabilidade e API de scoring.

## Como rodar (resumo)
- Colab: `notebooks/Credit_Scoring_EndToEnd.ipynb` → executa tudo e exporta CSVs para `dashboards/export/`.
- Local:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate   # Windows | source .venv/bin/activate (Linux/Mac)
  pip install -r requirements.txt
  python scripts/train_export.py
  ```
- API:
  ```bash
  pip install fastapi uvicorn shap joblib pydantic
  uvicorn api.main:app --reload
  # http://localhost:8000/health | /docs
  ```
