import pandas as pd
import os

BASE = "DBs/"

def load(file):
    path = BASE + file

    try:
        df = pd.read_json(path)
    except:
        df = pd.DataFrame()

    expected_columns = {
        "session_id": "object",
        "gambler_id": "object",
        "status": "object",
        "params": "object",
        "start_time": "object",
        "end_time": "object",
        "games_played": "int",
        "pause_time": "float",
        "end_reason": "object"
    }

    for col, dtype in expected_columns.items():
        if col not in df.columns:
            df[col] = None

        df[col] = df[col].astype("object")

    return df

def save(df, file):
    df.to_json(BASE + file, orient="records", indent=2)