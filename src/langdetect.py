import os

import pandas as pd

from utils.paths import resources_csv_dataframes
from utils.run_jar import get_lang_predict
from utils.time_wrap import timer_time


@timer_time  # Runs around 470 seconds
def classify_langdetect(dataframe=pd.DataFrame(), comp_method=str(), dataset_type=str()):
    identifier = LangDetect()
    li = dataframe['keyword'].tolist()
    lan_li = identifier.guess_language(li, comp_method)
    score = [lan[lan.find(":") + 1:lan.find(",")] for lan in lan_li]
        # score = lan[3:]
        # print(score)
    lan_li = [lan[:2] for lan in lan_li]
    lst = list(zip(li, lan_li, score))
    df = pd.DataFrame(lst, columns=['keyword', 'lang', 'conf'])
    comp_method += '.csv'
    suffix = dataset_type + comp_method
    os.chdir(resources_csv_dataframes)
    df.to_csv(suffix)
    return df


class LangDetect:
    # @staticmethod
    # def guess_language(text=str(), comp_method=str()):
    #     return get_lang_predict(text, comp_method)

    @staticmethod
    def guess_language(li=list(), comp_method=str()):
        return get_lang_predict(li, comp_method)

# @deprecated
# def classify_langdetect(dataframe=pd.DataFrame(), comp_method=str(), dataset_type=str()):
#     identifier = LangDetect()
#     li = dataframe['keyword'].tolist()
#     lst = list()
#     for entry in li:
#         lan = identifier.guess_language(entry, comp_method)
#         # print(lan)
#         score = lan[lan.find(":") + 1:lan.find(",")]
#         # score = lan[3:]
#         # print(score)
#         lan = lan[:2]
#         lst.append((entry, lan, score))
#     df = pd.DataFrame(lst, columns=['keyword', 'lang', 'conf'])
#     comp_method += '.csv'
#     suffix = dataset_type + comp_method
#     os.chdir(resources_csv_dataframes)
#     df.to_csv(suffix)
#     return df