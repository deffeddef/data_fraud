import pickle
from sklearn.preprocessing import MinMaxScaler
import category_encoders as ce


def loo_mms(df):
    loo = pickle.load(open('pickled_models/cat_enc_loo.sav', 'rb'))
    df_loo = loo.transform(df)
    mms = pickle.load(open('pickled_models/scaler_mms.sav', 'rb'))
    num_cols = ['Duration in month', 'Credit amount', 'Installment rate in percentage of disposable income',
                'Present residence since', 'Age', 'Number of existing credits at this bank',
                'Number of people being liable to provide maintenance for']

    df_loo[num_cols] = mms.transform(df_loo[num_cols])
    return df_loo