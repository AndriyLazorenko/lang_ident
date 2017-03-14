import os
from subprocess import Popen, PIPE, STDOUT

from utils.time_wrap import timer_time


def create_file(text):
    test_dir = '/home/andriy/Code/IdeaProjects/language-detection/tests'
    os.chdir(test_dir)
    path = 'temp.txt'
    # print(path)
    with open(path, 'w') as fh:
        fh.write(text)
    path = os.path.join(test_dir, path)
    return path


# @timer_time  # Average runtime of 0.7 seconds
def get_lang_predict(text=str):
    filepath = create_file(text)
    os.chdir('/home/andriy/Code/IdeaProjects/language-detection')
    p = Popen(['java', '-jar', "lib/langdetect.jar", '--detectlang',
               '-d', 'profiles_old', filepath], stdout=PIPE, stderr=STDOUT)
    li = list()
    for line in p.stdout:
        li.append(str(line))
    s = li[0]
    m = s[s.find("[") + 1:s.find("]")]
    delete_file()
    # print(m)
    return m


def delete_file():
    test_dir = '/home/andriy/Code/IdeaProjects/language-detection/tests'
    os.chdir(test_dir)
    path = 'temp.txt'
    os.remove(path)
