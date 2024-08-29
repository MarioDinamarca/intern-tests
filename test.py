import pandas as pd
import re

def clean_dataframe(df):
    for col in df.columns:
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x,str) else x)

        df[col] = df[col].apply(lambda x: re.sub(r'\W+', '',x) if isinstance(x,str) else x)

        df[col].fillna('', inplace=1)
    
    return df

interns = pd.read_csv('data/interns.csv')

interns_clean = clean_dataframe(interns)

interns_clean.to_excel('respuestas/mario_test1.xlsx',index=0)

