import os, json, pathlib, urllib.request, warnings
warnings.filterwarnings('ignore')
import pandas as pd, numpy as np, joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score, precision_score, recall_score
from xgboost import XGBClassifier
from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import Pipeline as ImbPipeline
from src.utils import robust_read_credit_card_csv, downcast_numeric
from src.pipeline import build_preprocess, infer_feature_types

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / 'data'
MODELS_DIR = PROJECT_ROOT / 'models'
MODELS_DIR.mkdir(parents=True, exist_ok=True)

def download_data():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    urls = [
        'https://raw.githubusercontent.com/ArinB/MSDS-422/master/Week5/UCI_Credit_Card.csv',
        'https://raw.githubusercontent.com/kirenz/datasets/master/uci_credit_card.csv'
    ]
    csv_path = DATA_DIR / 'UCI_Credit_Card.csv'
    for u in urls:
        try:
            print('Downloading', u)
            urllib.request.urlretrieve(u, csv_path)
            print('Saved to', csv_path)
            return csv_path
        except Exception as e:
            print('Failed', u, e)
    raise RuntimeError('Could not download dataset automatically. Place CSV at data/UCI_Credit_Card.csv')

def main():
    csv_path = download_data()
    df = robust_read_credit_card_csv(str(csv_path))
    df = downcast_numeric(df)
    target = 'target_default'
    num_cols, cat_cols = infer_feature_types(df, target)

    X = df.drop(columns=[target])
    y = df[target].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, stratify=y, random_state=42)
    preprocess = build_preprocess(num_cols, cat_cols)

    clf = XGBClassifier(
        n_estimators=400, max_depth=6, learning_rate=0.1,
        subsample=0.8, colsample_bytree=0.8,
        random_state=42, reg_lambda=1.0, n_jobs=-1,
        eval_metric='logloss', tree_method='hist'
    )

    pipe = ImbPipeline(steps=[('pre', preprocess), ('ros', RandomOverSampler(random_state=42)), ('clf', clf)])
    pipe.fit(X_train, y_train)

    proba = pipe.predict_proba(X_test)[:,1]
    preds = (proba >= 0.5).astype(int)
    metrics = {
        'auc': float(roc_auc_score(y_test, proba)),
        'f1': float(f1_score(y_test, preds)),
        'precision': float(precision_score(y_test, preds)),
        'recall': float(recall_score(y_test, preds)),
        'positives_test': float(y_test.mean())
    }
    print('Test metrics:', metrics)

    # Train artifacts for serving (no oversampling at inference)
    preprocess.fit(X_train, y_train)
    X_train_tr = preprocess.transform(X_train)

    clf_final = XGBClassifier(
        n_estimators=400, max_depth=6, learning_rate=0.1,
        subsample=0.8, colsample_bytree=0.8,
        random_state=42, reg_lambda=1.0, n_jobs=-1,
        eval_metric='logloss', tree_method='hist'
    )
    clf_final.fit(X_train_tr, y_train)

    joblib.dump(preprocess, MODELS_DIR/'preprocess.pkl')
    joblib.dump(clf_final, MODELS_DIR/'model_xgb.pkl')

    # Decision policy thresholds around best F1
    thresholds = np.linspace(0.05, 0.95, 19)
    from sklearn.metrics import f1_score
    proba_test = clf_final.predict_proba(preprocess.transform(X_test))[:,1]
    f1s = [f1_score(y_test, (proba_test>=t).astype(int)) for t in thresholds]
    best_thr = float(thresholds[int(np.argmax(f1s))])
    policy = {
        'approve_threshold': max(0.05, round(best_thr - 0.25, 2)),
        'review_threshold': round(best_thr, 2),
        'deny_threshold': min(0.95, round(best_thr + 0.25, 2))
    }
    meta = {
        'feature_order': list(X.columns),
        'num_cols': num_cols,
        'cat_cols': cat_cols,
        'target': target,
        'metrics_test': metrics,
        'model': 'XGBClassifier',
        'version': '1.0.0'
    }
    (MODELS_DIR/'thresholds.json').write_text(json.dumps(policy, indent=2))
    (MODELS_DIR/'metadata.json').write_text(json.dumps(meta, indent=2))
    print('Artifacts ->', MODELS_DIR.resolve())
    print('Policy ->', policy)

if __name__ == '__main__':
    main()
