from sklearn.metrics import brier_score_loss
from xgboost import XGBClassifier
import warnings
import pickle


def predictor(df):
    xg_cal = pickle.load(open('pickled_models/xg_cal_fully_fit.sav', 'rb'))
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        proba_pred = xg_cal.predict_proba(df)[:, 1]
    goodbad = []
    for proba in proba_pred:
        if proba >= .74:
            goodbad.append('good')
        else:
            goodbad.append('bad')
    df['results'] = goodbad

    return df