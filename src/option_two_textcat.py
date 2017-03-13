import os

import nltk.classify as cl
import pandas as pd


def classify_nltk(dataframe=pd.DataFrame(), comp_method=str, dataset_type=str):
    identifier = cl.TextCat()
    li = dataframe['keyword'].tolist()
    lst = list()
    for entry in li:
        lan = identifier.guess_language(entry)
        lan = lan[:2]
        lst.append((entry, lan, 1))
    df = pd.DataFrame(lst, columns=['keyword', 'lang', 'conf'])
    comp_method += '.csv'
    suffix = dataset_type + comp_method
    path = os.path.join('../resources/csv/dataframes', suffix)
    df.to_csv(path)
    return df
