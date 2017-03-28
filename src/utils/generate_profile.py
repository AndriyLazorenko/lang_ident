import json
import os

import time

'''
Do not use directly. This python file is made for communication with my local cluster at home (I have a server)
It is here for informational purpose only
'''

env_python = "/home/loki/miniconda3/envs/spark-lang/bin/python3"
text_path = '/home/loki/Datasets/dewiki.xml'
out_path = 'de.json'
partition_num = 100

os.environ.setdefault('PYSPARK_PYTHON', env_python)
# os.environ.setdefault('PYSPARK_DRIVER_PYTHON', "/home/andriy/anaconda3/envs/spark/bin/ipython3")

from pyspark.sql import SparkSession

spark = SparkSession.builder. \
    master("spark://192.168.1.46:7077"). \
    appName("lang_profile_generation"). \
    getOrCreate()

sc = spark.sparkContext

from sklearn import feature_extraction

f = feature_extraction.text.CountVectorizer()
anal = f.build_analyzer()


def word2grams(start=int, end=int, word=str):
    li = list()
    for n in range(start, end):
        l = [word[i:i + n] for i in range(len(word) - n + 1)]
        if l:
            li.extend(l)
    return li


def tokenizer(line):
    tokens = anal(line)
    return tokens


def n_gramizer(word):
    return word2grams(1, 10, word)

fh = open(text_path)
textFile = sc.parallelize(fh, partition_num)

t1 = time.time()
res = textFile.flatMap(lambda line: tokenizer(line)) \
    .flatMap(lambda word: n_gramizer(word)) \
    .map(lambda gram: (gram, 1)) \
    .reduceByKey(lambda a, b: a + b)

with open(out_path, 'w') as fp:
    json.dump(dict(res.collect()), fp)

t2 = time.time() - t1
print(t2)
