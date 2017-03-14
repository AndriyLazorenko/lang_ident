import os

import pandas as pd

from utils.run_jar import get_lang_predict
from utils.time_wrap import timer_time


@timer_time  # Runs around 470 seconds
def classify_langdetect(dataframe=pd.DataFrame(), comp_method=str, dataset_type=str):
    identifier = LangDetect()
    li = dataframe['keyword'].tolist()
    lst = list()
    for entry in li:
        lan = identifier.guess_language(entry)
        # print(lan)
        score = lan[lan.find(":") + 1:lan.find(",")]
        # score = lan[3:]
        # print(score)
        lan = lan[:2]
        lst.append((entry, lan, score))
    df = pd.DataFrame(lst, columns=['keyword', 'lang', 'conf'])
    comp_method += '.csv'
    suffix = dataset_type + comp_method
    os.chdir('/home/andriy/Code/PyCharmProjects/lang_ident/resources/csv/dataframes')
    df.to_csv(suffix)
    return df


class LangDetect():
    @staticmethod
    def guess_language(text=str):
        return get_lang_predict(text)
