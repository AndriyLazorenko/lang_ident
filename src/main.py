import os

import pandas as pd
import json
from utils import paths

from eval import compare
from langdetect import classify_langdetect

from option_one_langid import classify_langid
from option_two_textcat import classify_nltk


# load ground truth data


def load_ground_truth():
    real = pd.read_csv(paths.ground_truth_real_csv, sep='\t',
                       names=["keyword", "lang"])
    ideal = pd.read_csv(paths.ground_truth_ideal_csv, sep='\t',
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
        path = os.path.join(paths.dataframes, comp_method)
        df.to_csv(path)
    return df


real, ideal = load_ground_truth()


# sort-of-factory to load different classification methods
def classify(dataset=pd.DataFrame(), comp_method=str, dataset_type=str):
    if comp_method == 'langid':
        return classify_langid(dataset, comp_method, dataset_type)
    elif comp_method == 'lang_detect':
        return classify_langdetect(dataset, comp_method, dataset_type)
    elif comp_method == 'nltk':
        return classify_nltk(dataset, comp_method, dataset_type)
    elif comp_method == 'lang_nine':
        return classify_langdetect(dataset, comp_method, dataset_type)
    elif comp_method == 'lang_six':
        return classify_langdetect(dataset, comp_method, dataset_type)


# compare ground truth with langdetect
def compare_ground_langdetect():
    comp_method = 'lang_detect'
    real_ld = classify(real, comp_method, 'real')
    ideal_ld = classify(ideal, comp_method, 'ideal')
    compare(real, real_ld, 'real', comp_method)
    compare(ideal, ideal_ld, 'ideal', comp_method)


comp_path_id = os.path.isfile(paths.ideallangdetect_csv)
comp_path_re = os.path.isfile(paths.reallangdetect_csv)


def load_comp_gr_detect():
    real_ld = pd.DataFrame.from_csv(paths.reallangdetect_csv)
    ideal_ld = pd.DataFrame.from_csv(paths.ideallangdetect_csv)
    compare(real, real_ld, 'real', 'langdetect')
    compare(ideal, ideal_ld, 'ideal', 'langdetect')


if not comp_path_id and not comp_path_re:
    compare_ground_langdetect()
else:
    load_comp_gr_detect()


# compare ground truth with baseline
# def compare_ground_baseline():
#     real_e = load_bad_json(paths.real_json, 'real')
#     ideal_e = load_bad_json(paths.ideal_json, 'ideal')
#     compare(real, real_e, 'real', 'baseline')
#     compare(ideal, ideal_e, 'ideal', 'baseline')
#
#
# comp_path_id = os.path.isfile(paths.idealbaseline_csv)
# comp_path_re = os.path.isfile(paths.realbaseline_csv)
#
#
# def load_comp_gr_base():
#     real_e = pd.DataFrame.from_csv(paths.realbaseline_csv)
#     ideal_e = pd.DataFrame.from_csv(paths.idealbaseline_csv)
#     compare(real, real_e, 'real', 'baseline')
#     compare(ideal, ideal_e, 'ideal', 'baseline')
#
#
# if not comp_path_id and not comp_path_re:
#     compare_ground_baseline()
# else:
#     load_comp_gr_base()


# compare ground truth with langid
# def compare_ground_langid():
#     comp_method = 'langid'
#     real_l = classify(real, comp_method, 'real')
#     ideal_l = classify(ideal, comp_method, 'ideal')
#     compare(real, real_l, 'real', comp_method)
#     compare(ideal, ideal_l, 'ideal', comp_method)
#
#
# comp_path_id = os.path.isfile(paths.ideallangid_csv)
# comp_path_re = os.path.isfile(paths.reallangid_csv)
#
#
# def load_comp_gr_id():
#     real_l = pd.DataFrame.from_csv(paths.reallangid_csv)
#     ideal_l = pd.DataFrame.from_csv(paths.ideallangid_csv)
#     compare(real, real_l, 'real', 'langid')
#     compare(ideal, ideal_l, 'ideal', 'langid')
#
#
# if not comp_path_id and not comp_path_re:
#     compare_ground_langid()
# else:
#     load_comp_gr_id()





# Compare ground truth with langdetect on 6-grams

def compare_ground_six():
    comp_method = 'lang_six'
    real_si = classify(real, comp_method, 'real')
    ideal_si = classify(ideal, comp_method, 'ideal')
    compare(real, real_si, 'real', comp_method)
    compare(ideal, ideal_si, 'ideal', comp_method)


comp_path_id = os.path.isfile(paths.idealsix_csv)
comp_path_re = os.path.isfile(paths.realsix_csv)


def load_comp_gr_six():
    real_ni = pd.DataFrame.from_csv(paths.realsix_csv)
    ideal_ni = pd.DataFrame.from_csv(paths.idealsix_csv)
    compare(real, real_ni, 'real', 'lang_six')
    compare(ideal, ideal_ni, 'ideal', 'lang_six')


if not comp_path_id and not comp_path_re:
    compare_ground_six()
else:
    load_comp_gr_six()


# compare ground truth with langdetect on 9-grams

# def compare_ground_nine():
#     comp_method = 'lang_nine'
#     real_ni = classify(real, comp_method, 'real')
#     ideal_ni = classify(ideal, comp_method, 'ideal')
#     compare(real, real_ni, 'real', comp_method)
#     compare(ideal, ideal_ni, 'ideal', comp_method)
#
#
# comp_path_id = os.path.isfile(paths.idealnine_csv)
# comp_path_re = os.path.isfile(paths.realnine_csv)
#
#
# def load_comp_gr_nine():
#     real_ni = pd.DataFrame.from_csv(paths.realnine_csv)
#     ideal_ni = pd.DataFrame.from_csv(paths.idealnine_csv)
#     compare(real, real_ni, 'real', 'lang_nine')
#     compare(ideal, ideal_ni, 'ideal', 'lang_nine')
#
#
# if not comp_path_id and not comp_path_re:
#     compare_ground_nine()
# else:
#     load_comp_gr_nine()


# compare ground truth with nltk
##=============================================================
# comp_method = 'nltk'
# real_n = classify(real, comp_method, 'real')
# ideal_n = classify(ideal, comp_method, 'ideal')
#
# compare(real, real_n, 'real', comp_method)
# compare(ideal, ideal_n, 'ideal', comp_method)
##=============================================================
