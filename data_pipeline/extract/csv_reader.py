import pandas as pd

def read_csv(path, sep=";"):
    return pd.read_csv(path, sep=sep)