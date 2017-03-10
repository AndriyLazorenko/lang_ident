import pandas as pd
from langid.langid import LanguageIdentifier, model


# method for classification of language with langid. Lousy model, worse than baseline ot ground_truth
# however, can be trained on relevant data to perform better

def classify_langid(dataframe):
    identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
    li = dataframe['keyword'].tolist()
    lst = list()
    for entry in li:
        lst.append((entry, identifier.classify(entry)[0], identifier.classify(entry)[1]))
    df = pd.DataFrame(lst, columns=['keyword', 'lang', 'conf'])
    return df
