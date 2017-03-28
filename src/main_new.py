import os

import pandas as pd
from utils import paths

from eval import compare
from langdetect import classify_langdetect

from option_one_langid import classify_langid
from option_two_textcat import classify_nltk

# load ground truth data
from utils.cook_dataset import cook


def load_ground_truth():
    tru = cook()
    return tru


truth = load_ground_truth()


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


# Compare ground truth with baseline
def comp_gr_ld():
    def compare_ground_langdetect(trth=pd.DataFrame(), dataset=pd.DataFrame(), dataset_type='new',
                                  comp_method='lang_detect'):
        ld = classify(dataset, comp_method, dataset_type)
        compare(trth, ld, dataset_type, comp_method)

    def load_comp_gr_detect(trth=pd.DataFrame(), dataset_type='new', comp_method='lang_detect',
                            dataset_path=paths.ld_res):
        ld = pd.DataFrame.from_csv(dataset_path)
        compare(trth, ld, dataset_type, comp_method)

    comp_path = os.path.isfile(paths.ld_res)

    if not comp_path:
        compare_ground_langdetect(trth=truth, dataset=truth)
    else:
        load_comp_gr_detect(trth=truth)


comp_gr_ld()


# Compare ground truth with langdetect on 6-grams
def comp_gr_si():
    def compare_ground_six(trth=pd.DataFrame(), dataset=pd.DataFrame(), dataset_type='new',
                           comp_method='lang_six'):
        si = classify(dataset, comp_method, dataset_type)
        compare(trth, si, dataset_type, comp_method)

    def load_comp_gr_six(trth=pd.DataFrame(), dataset_type='new', comp_method='lang_six',
                         dataset_path=paths.si_res):
        si = pd.DataFrame.from_csv(dataset_path)
        compare(trth, si, dataset_type, comp_method)

    comp_path = os.path.isfile(paths.si_res)
    if not comp_path:
        compare_ground_six(trth=truth, dataset=truth)
    else:
        load_comp_gr_six(trth=truth)


comp_gr_si()

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
