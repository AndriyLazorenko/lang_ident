import csv
import os

import sklearn.metrics as metrics


def compare(data, pred_data, data_prop, method):
    y_pred = pred_data[['lang']]
    y_actual = data[['lang']]
    acu = metrics.accuracy_score(y_pred=y_pred, y_true=y_actual)
    f_one = metrics.f1_score(y_pred=y_pred, y_true=y_actual, average='weighted')
    print('Tested on', data_prop, 'data, with', method)
    print('Accuracy =', str("{0:.3g}".format(acu)), 'F1 =', "{0:.3g}".format(f_one))
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open('../resources/csv/compare_results/res.csv', 'a') as fh:
        wr = csv.writer(fh, dialect='excel')
        wr.writerow([method, data_prop, str(acu), str(f_one)])
    # Optional - print confusion matrix

    # conf = metrics.confusion_matrix(y_pred=y_pred, y_true=y_actual)
    # print(conf)


