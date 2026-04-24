import pandas as pd
import os

BASE = "DBs/"

def load(file):
    path = BASE + file
    if not os.path.exists(path):
        return pd.DataFrame()
    return pd.read_json(path)

def save(df, file):
    df.to_json(BASE + file, orient="records", indent=2)