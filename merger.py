#import pandas as pd

def merger (df, ci):
    df['Credit Identifier'] = ci
    df = df[['Credit Identifier', 'results']]
    return df