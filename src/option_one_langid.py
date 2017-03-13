import os

import pandas as pd
from langid.langid import LanguageIdentifier, model


# method for classification of language with langid. Lousy model, worse than baseline ot ground_truth
# however, can be trained on relevant data to perform better
# https://github.com/saffsd/langid.py

def classify_langid(dataframe=pd.DataFrame(), comp_method=str, dataset_type=str):
    identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
    li = dataframe['keyword'].tolist()
    lst = list()
    for entry in li:
        lst.append((entry, identifier.classify(entry)[0], identifier.classify(entry)[1]))
    df = pd.DataFrame(lst, columns=['keyword', 'lang', 'conf'])
    comp_method += '.csv'
    suffix = dataset_type + comp_method
    path = os.path.join('../resources/csv/dataframes', suffix)
    df.to_csv(path)
    return df
