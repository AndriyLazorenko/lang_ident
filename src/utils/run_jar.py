import glob
import os
from subprocess import Popen, PIPE, STDOUT

from utils.paths import test_dir, language_detection
from utils.time_wrap import timer_time


def create_file(text=str(), ind=int()):
    os.chdir(test_dir)
    path = str(ind) + '.txt'
    # print(path)
    with open(path, 'w') as fh:
        fh.write(text)
    path = os.path.join(test_dir, path)
    return path


# @timer_time  # Average runtime of 0.7 seconds
def get_lang_predict(text=list(), comp_method=str()):
    paths = list()
    for ind, entry in enumerate(text):
        path = create_file(entry, ind)
        paths.append(path)
    os.chdir(language_detection)
    jar6_path = 'lib/langdetect-1.1-20160603.jar'
    jar3_path = 'lib/langdetect.jar'
    p3 = 'profiles3'
    p6 = 'profiles'
    # fps = str(paths).strip('[]')
    # query = get_query()
    res = list()
    if comp_method == 'lang_detect':
        qry = get_query(jar_variant=jar3_path, profile_variant=p3, paths=paths)
        # print (qry[5])
        p = Popen(qry, stdout=PIPE, stderr=STDOUT)
        li = list()
        for line in p.stdout:
            li.append(str(line))
        for entry in li:
            s = entry
            # print(s)
            m = s[s.find("[") + 1:s.find("]")]
            res.append(m)
    elif comp_method == 'lang_six':
        qry = get_query(jar_variant=jar6_path, profile_variant=p6, paths=paths)
        p = Popen(qry, stdout=PIPE, stderr=STDOUT)
        li = list()
        for line in p.stdout:
            li.append(str(line))
        res = list()
        for entry in li:
            s = entry
            #     print(s)
            if 'NGram' in entry:
                continue
            elif 'NGam' in entry:
                continue
            else:
                m = s[s.find("[") + 1:s.find("]")]
                res.append(m)
    else:
        qry = get_query(jar_variant=jar6_path, profile_variant=p6, paths=paths)
        p = Popen(qry, stdout=PIPE, stderr=STDOUT)
        li = list()
        for line in p.stdout:
            li.append(str(line))
        res = list()
        for entry in li:
            s = entry
            #     print(s)
            if 'NGram' in entry:
                continue
            elif 'NGam' in entry:
                continue
            else:
                m = s[s.find("[") + 1:s.find("]")]
                res.append(m)
    return res


def get_query(jar_variant=str(), profile_variant=str(), paths=list()):
    query = list()
    query.append('java')
    if profile_variant=='profiles3':
        query.append('-jar')
        query.append(jar_variant)
    elif profile_variant=='profiles':
        query.append('-cp')
        query.append('lib/langdetect-1.1-20160603.jar:lib/jsonic-1.2.0.jar')
        query.append('com.cybozu.labs.langdetect.Command')
    query.append('--detectlang')
    query.append('-d')
    query.append(profile_variant)
    query.append('-s')
    query.append('0')
    for path in paths:
        query.append(path)
    # print(query)
    return query


# @deprecated
# def get_lang_predict(text=str, comp_method=str):
#     filepath = create_file(text)
#     os.chdir(language_detection)
#     jar6_path = 'lib/langdetect-1.1-20160603.jar'
#     jar3_path = 'lib/langdetect.jar'
#     if comp_method == 'lang_detect':
#         p = Popen(['java', '-jar', jar3_path, '--detectlang',
#                    '-d', 'profiles3', '-s', '0', filepath], stdout=PIPE, stderr=STDOUT)
#     elif comp_method == 'lang_six':
#         p = Popen(['java', '-jar', jar6_path, '--detectlang',
#                    '-d', 'profiles', '-s', '0', filepath], stdout=PIPE, stderr=STDOUT)
#     else:
#         p = Popen(['java', '-jar', jar6_path, '--detectlang',
#                    '-d', 'profiles_9', '-s', '0', filepath], stdout=PIPE, stderr=STDOUT)
#     li = list()
#     for line in p.stdout:
#         li.append(str(line))
#     s = li[0]
#     m = s[s.find("[") + 1:s.find("]")]
#     delete_file()
#     # print(m)
#     return m


# def delete_file():
#     os.chdir(test_dir)
#     path = 'temp.txt'
#     os.remove(path)



def delete_files():
    files = glob.glob(test_dir+'/*')
    # print(files)
    for f in files:
        os.remove(f)
