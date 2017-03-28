import json

from collections import defaultdict

path_in = '/home/andriy/Code/IdeaProjects/language-detection/profiles_9/en.json'
path_out = '/home/andriy/Code/IdeaProjects/language-detection/profiles_9/en_clean.json'


def cook_profile(path, lang):
    with open(path, 'r') as fh:
        profile = json.load(fh)
    # print(profile['a']) # DEBUG
    counts = defaultdict(int)
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for key in profile:
        if len(key) in lst:
            counts[len(key)] += profile[key]
    counts = dict(counts)
    li_cnts = list()
    for i in range(1, 10):
        li_cnts.append(counts[i])
    out = dict()
    out['freq'] = profile
    out['name'] = lang
    out['n_words'] = li_cnts
    with open(path, 'w') as fh:
        json.dump(out, fh)


def cook_profiles():
    common_path = '/home/andriy/Code/IdeaProjects/language-detection/profiles_9/'
    langs = ['en', 'de', 'fr']
    for lan in langs:
        pth = common_path + lan + '.json'
        cook_profile(pth, lan)


# cook_profile(path, 'en')

def test_profile(path):
    with open(path, 'r') as fh:
        profile = json.load(fh)
    print(profile['name'])
    print(profile['n_words'])
    print(profile['freq'])


# test_profile(path)


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def clean_profile(pth_in, pth_out, div_factor=100000):
    """
    Method accepts messy json with chargrams and cleanses them of evil!
    Evil comes in two forms: numbers and infrequent chargrams
    They're evil because they are noise and don't help classifier in any reasonable way
    Chargram
    :param pth_in: path of messy json
    :param pth_out: path of cleansed json
    :param div_factor: is an interesting param that sets a threshold for infrequent chargrams.
    It works as follows: chargram is thrown if less frequent than total number of chargrams in
    respective n (length of chargram) category, divided by div_factor. div_factor of 100000 seems
    to do the job (balance between noise and precision).
    :return:
    """
    with open(pth_in, 'r') as fh:
        profile = json.load(fh)
    chargrams = profile['freq']
    n_words = profile['n_words']
    for cg in list(chargrams):
        if hasNumbers(cg):
            chargrams.pop(cg)
        elif chargrams[cg] < (n_words[len(cg) - 1] / div_factor):
            chargrams.pop(cg)
    profile['freq'] = chargrams
    with open(pth_out, 'w') as fh:
        json.dump(profile, fh)


clean_profile(path_in, path_out)
test_profile(path_out)
