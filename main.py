import sys
import pandas as pd
from merger import merger
from predictor import predictor
from transformer import loo_mms
from renamer import df_renamer

if __name__ == '__main__':

    in_file, out_file = sys.argv[1:]

    df = pd.read_csv(in_file)
    df, ci = df_renamer(df)
    df = loo_mms(df)
    prediction = predictor(df)
    result = merger(df,ci)

    result.to_csv(out_file, index=False)
    print ('Prediction Successful!...Please Check CSV File for Results')
