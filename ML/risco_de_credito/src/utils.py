import pandas as pd
import numpy as np

def robust_read_credit_card_csv(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    # UCI target column contains 'default'
    target_candidates = [c for c in df.columns if 'default' in c]
    if not target_candidates:
        raise ValueError("Could not find target column ('default') in CSV.")
    target_col = target_candidates[-1]
    df = df.rename(columns={target_col: 'target_default'})
    return df

def downcast_numeric(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include=['int64','int32']).columns:
        df[col] = pd.to_numeric(df[col], downcast='integer')
    for col in df.select_dtypes(include=['float64','float32']).columns:
        df[col] = pd.to_numeric(df[col], downcast='float')
    return df
