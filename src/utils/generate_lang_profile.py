import os

from subprocess import Popen, PIPE, STDOUT

from utils.paths import lang_detect, datasets
from utils.time_wrap import timer_time



@timer_time
def generate_profile_old(lang=str):
    filename = lang + 'wiki.xml'
    filepath = os.path.join(datasets, filename)
    os.chdir(lang_detect)
    p = Popen(['java', '-jar', "lib/langdetect.jar", '--genprofile-text',
               '-l', lang, filepath], stdout=PIPE, stderr=STDOUT)




