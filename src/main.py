import pandas as pd
import json

from eval import compare

from langid_option_one import classify_langid


# load ground truth data

def load_ground_truth():
    real = pd.read_csv('../resources/csv/ground_truth/real.csv', sep='\t',
                       names=["keyword", "lang"])
    ideal = pd.read_csv('../resources/csv/ground_truth/ideal.csv', sep='\t',
                        names=["keyword", "lang"])
    return real, ideal


# load data processed with classifier
def load_bad_json(path):
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
    return df


real_e = load_bad_json('../resources/csv/current_classifier/real.json')
ideal_e = load_bad_json('../resources/csv/current_classifier/ideal.json')

real, ideal = load_ground_truth()

# compare ground truth with baseline
compare(real, real_e, 'real', 'baseline')
compare(ideal, ideal_e, 'ideal', 'baseline')

real_l = classify_langid(real)
ideal_l = classify_langid(ideal)

# compare ground truth with langid
compare(real, real_l, 'real', 'langid')
compare(ideal, ideal_l, 'ideal', 'langid')
