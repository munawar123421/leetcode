import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    concatenation=[df1,df2]
    return pd.concat(concatenation)