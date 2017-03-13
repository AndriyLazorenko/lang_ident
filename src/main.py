import os

import pandas as pd
import json

from eval import compare

from option_one_langid import classify_langid


# load ground truth data
from option_two_textcat import classify_nltk


def load_ground_truth():
    real = pd.read_csv('../resources/csv/ground_truth/real.csv', sep='\t',
                       names=["keyword", "lang"])
    ideal = pd.read_csv('../resources/csv/ground_truth/ideal.csv', sep='\t',
                        names=["keyword", "lang"])
    return real, ideal


# load data processed with classifier
def load_bad_json(path, type):
    comp_method = type + 'baseline'
    with open(path, "r") as f:
        jso = json.load(f)
        lst = list()
        for entry in jso:
            ent_split = entry.split('DetectedLanguage')
            keyword = ent_split[0]
            tup = ent_split[1]
            tup = tup.strip('()')
            tup_split = tup.split(',')
            lst.append((keyword, tup_split[0], tup_split[1]))
        df = pd.DataFrame(lst, columns=['keyword', 'lang', 'conf'])
        comp_method += '.csv'
        path = os.path.join('../resources/csv/dataframes', comp_method)
        df.to_csv(path)
    return df

real, ideal = load_ground_truth()

# compare ground truth with baseline
real_e = load_bad_json('../resources/csv/current_classifier/real.json', 'real')
ideal_e = load_bad_json('../resources/csv/current_classifier/ideal.json', 'ideal')

compare(real, real_e, 'real', 'baseline')
compare(ideal, ideal_e, 'ideal', 'baseline')

# compare ground truth with langid
comp_method = 'langid'
real_l = classify_langid(real, comp_method, 'real')
ideal_l = classify_langid(ideal, comp_method, 'ideal')

compare(real, real_l, 'real', comp_method)
compare(ideal, ideal_l, 'ideal', comp_method)

# compare ground truth with nltk
comp_method = 'nltk'
real_n = classify_nltk(real, comp_method, 'real')
ideal_n = classify_nltk(ideal, comp_method, 'ideal')

compare(real, real_n, 'real', comp_method)
compare(ideal, ideal_n, 'ideal', comp_method)
