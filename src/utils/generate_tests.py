import csv
import os


def generate_tests(texts=list):
    for ind, item in enumerate(texts):
        path = item + '.txt'
        os.chdir('/home/andriy/Code/PyCharmProjects/lang_ident/src/utils/tests_files')
        with open(path, 'w') as f:
            f.write(item)


def purge_tests():
    folder = 'test_files'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def load_tests_jira():
    res = list()
    with open('../../resources/csv/tests_jira.csv', 'r') as fh:
        # res = fh.readlines()
        reader = csv.reader(fh)
        for line in reader:
            res.append(line[0])
        return res


def init_jira_tests():
    li = load_tests_jira()
    generate_tests(li)

init_jira_tests()

