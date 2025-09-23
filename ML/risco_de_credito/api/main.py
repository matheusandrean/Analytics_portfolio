from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any
import joblib, json, pathlib, numpy as np
import shap

app = FastAPI(title="Credit Scoring API", version="1.0.0")
ROOT = pathlib.Path(__file__).resolve().parents[1]
MODELS_DIR = ROOT / 'models'

preprocess = None
model = None
policy = None
metadata = None
feature_order = None
explainer = None

@app.on_event("startup")
def _load():
    global preprocess, model, policy, metadata, feature_order, explainer
    preprocess = joblib.load(MODELS_DIR/'preprocess.pkl')
    model = joblib.load(MODELS_DIR/'model_xgb.pkl')
    policy = json.loads((MODELS_DIR/'thresholds.json').read_text())
    metadata = json.loads((MODELS_DIR/'metadata.json').read_text())
    feature_order = metadata['feature_order']
    explainer = shap.TreeExplainer(model)

class CreditApplication(BaseModel):
    data: Dict[str, float] = Field(..., description="feature -> value")

def _row(payload: Dict[str, Any]) -> np.ndarray:
    missing = [c for c in feature_order if c not in payload]
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing fields: {missing[:10]} ...")
    arr = [payload[c] for c in feature_order]
    return np.array(arr, dtype=float).reshape(1, -1)

def _decide(pd: float) -> Dict[str, Any]:
    a, r, d = policy['approve_threshold'], policy['review_threshold'], policy['deny_threshold']
    if pd <= a:
        return {"decision": "APPROVE", "reason": "Low PD (<= approve threshold)", "thresholds": policy}
    if pd <= r:
        return {"decision": "APPROVE_WITH_LOW_LIMIT", "reason": "PD between approve and review", "thresholds": policy}
    if pd <= d:
        return {"decision": "REVIEW", "reason": "Intermediate PD (manual review)", "thresholds": policy}
    return {"decision": "DENY", "reason": "High PD (>= deny threshold)", "thresholds": policy}

@app.get("/health")
def health():
    return {"status": "ok", "model": metadata.get("model"), "version": metadata.get("version")}

@app.post("/score")
def score(payload: CreditApplication):
    X = _row(payload.data)
    Xtr = preprocess.transform(X)
    pd = float(model.predict_proba(Xtr)[:,1][0])
    sv = explainer.shap_values(Xtr)
    shap_pos = sv[1][0] if isinstance(sv, list) else sv[0]
    idx = np.argsort(np.abs(shap_pos))[::-1][:5]
    reasons = [{"feature": feature_order[i], "impact": float(shap_pos[i])} for i in idx]
    return {"pd": pd, **_decide(pd), "top_reasons": reasons}
