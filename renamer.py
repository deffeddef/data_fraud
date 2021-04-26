import pandas as pd

def df_renamer(df):
    cols = ['Credit Identifier', 'Money on checking account', 'Duration in month', 'Credit History', 'Purpose',
            'Credit amount', 'Savings account/bonds','Current employment since',
            'Installment rate in percentage of disposable income', 'Personal status and sex',
            'Other debtors / guarantors', 'Present residence since', 'Property', 'Age', 'Other installment plans',
            'Housing', 'Number of existing credits at this bank', 'Job',
            'Number of people being liable to provide maintenance for', 'Telephone', 'Foreign worker']
    df.columns = cols

    moca = {11: "< 0", 12: "0 <= ... < 200", 13: "... >= 200", 14: "no checking account"}

    ch = {30: "no credits taken/ all credits paid back duly", 31: "all credits at this bank paid back duly",
          32: "existing credits paid back duly till now",
          33: "delay in paying off in the past", 34: "other credits existing (not at this bank)"}

    purp = {40: "car (new)", 41: "car (used)", 42: "furniture/equipment", 43: "radio/television",
            44: "domestic appliances", 45: "repairs", 46: "education", 47: "vacation",
            48: "retraining", 49: "business", 410: "others"}

    sab = {61: "... < 100 DM", 62: "100 <= ... < 500", 63: "500 <= ... < 1000", 64: ".. >= 1000", 65: "unknown"}

    ces = {71: "unemployed", 72: "... < 1 year", 73: "1 <= ... < 4 years", 4: "4 <= ... < 7 years", 75: ".. >= 7 years"}

    pss = {91: "male : divorced/separated", 92: "female : divorced/separated/married", 93: "male : single",
           94: "male : married/widowed",
           95: "female : single"}

    odg = {101: "none", 102: "co-applicant", 103: "guarantor"}

    prop = {121: "real estate", 122: "if not 121 : building society savings / life insurance",
            123: "if not 121/122 : car or other, not in attribute 6",
            124: "unknown / no property"}

    oip = {141: "bank", 142: "stores", 143: "none"}

    hou = {151: "rent", 152: "own", 153: "for free"}

    job = {171: "unemployed/ unskilled - non-resident", 172: "unskilled - resident", 173: "skilled employee / official",
           174: "management / self-employed / highly qualified employee / officer"}

    tel = {191: "none", 192: "yes, registered under the customers name"}

    fw = {201: "yes", 202: "no"}

    df = df.replace(
        {"Money on checking account": moca, "Credit History": ch, 'Purpose': purp, 'Savings account/bonds': sab,
         'Current employment since': ces,
         'Personal status and sex': pss, 'Other debtors / guarantors': odg, 'Property': prop,
         'Other installment plans': oip, 'Housing': hou,
         'Job': job, 'Telephone': tel, 'Foreign worker': fw})

    ci = df['Credit Identifier']
    df = df.drop('Credit Identifier', axis=1)
    return df, ci