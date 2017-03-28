import glob
import os
from time import sleep

import pandas as pd


def cook_paths():
    all_path = '/home/andriy/Code/PyCharmProjects/lang_ident/resources/csv/labeled_dataset'
    ret = dict()
    ret['en'] = os.path.join(all_path, 'en/all_in_one.csv')
    ret['de'] = os.path.join(all_path, 'de/german_learn_set.csv')
    ret['fr'] = os.path.join(all_path, 'fr/french_learning_set.csv')
    return ret


def cook():
    paths = cook_paths()
    li = list()
    for lang in paths.keys():
        df = pd.read_csv(paths[lang], names=['keyword', 'class'])
        df.drop(df.columns[[1]], axis=1, inplace=True)
        df['lang'] = lang
        li.append(df)
        # print(df) # DEBUG
    df = pd.concat(li)
    return df

