
#encoding=utf-8
import csv
import scipy.stats as stats
import argparse
import pandas as pd
import numpy as np
import time
import math
import csv
import argparse
import os
import pandas as pd
import numpy as np
import numpy
import matplotlib.pyplot as plt
from compiler.ast import flatten
import scipy.stats as stats
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--data_name',type=str,default='data/csxd_data/clic_csxd_test',help='training data in csv format')
parser.add_argument('--test_name',type=str,default='data/csxd_data/clic_csxd_test',help='training data in csv format')
parser.add_argument('--savename',type=str,default='data/csxd_data/clic_csxd_test_des.csv',help='training data in csv format')
args = parser.parse_args()
def load_data(path):
    return pd.read_csv(path, error_bad_lines=False)


def split_bin(delay, retain):
    delay_delay = pd.merge(delay, retain, on=['user'], how='outer')  # 传出数组
    groud_truth = np.array(delay_delay['retain'])
    delay_delay_time = np.array(delay['delay'])

    index = groud_truth != 1
    groud_truth[index] = 0  # if not 1, then transform to 0
    order = np.argsort(delay_delay_time)  # sort y_pred
    delay_delay_time_tmp = list(groud_truth[order])  # sort delay_delay_time according to y_pred
    # delay_delay_time_tmp.reverse()
    bin_spilt_path =  range(0,1000,100)
    len_bin  = [0]*11
    print len_bin,bin_spilt_path
    i = 0
    for ery in delay_delay_time_tmp:
        if ery <=bin_spilt_path[i]:
            len_bin[i]+=1
        else: i+=1
    group = [delay_delay_time_tmp[i * len_bin[i]:(i + 1) * len_bin[i]] for i in range(0, len(len_bin))]
    group.append(delay_delay_time_tmp[len_bin[-1] * len_bin[-1]:])
    group[-1] = flatten(group[-1][:])

    good_list = [sum(group[i]) for i in range(0, len(len_bin))]  # number of good for each group
    good_ks_result_list = [0]  # accumulated freq for good

    for i in range(1, len(len_bin) + 1):
        retention_rate = sum(group[i])*1.0/len(group[i])
        good_ks_result_list.append(retention_rate)


if __name__ == '__main__':
    print range(100,1100,100) ,[0]*11
    df1 = pd.DataFrame([1],columns=['retain'])
    print df1
    df1 =df1[df1['retain']-1]
    # print df1
    # df1['user'] = [[0, 0, 0]]
    # df2 = pd.DataFrame([-0.29947643 -1.2484097  -0.22411213],columns=['delay'])
    # df2 ['user']= [[0,0,0]]
    #
    # split_bin(df1, df2)

    # print range(0,1000,100)
    # groud_truth = np.array(delay_delay['retain'])
    # delay_delay_time = np.array(delay_delay['delay_delay'])
    # index = delay_delay_time != 1
    # delay_delay_time[index] = 0  # if not 1, then transform to 0
    # order = np.argsort(y_pred)  # sort y_pred
    # delay_delay_time_tmp = list(delay_delay_time[order])  # sort delay_delay_time according to y_pred
    # delay_delay_time_tmp.reverse()
    # num_bin = int(len(index) * 1.0 / 100)
    # group = [delay_delay_time_tmp[i * len_bin:(i + 1) * len_bin] for i in range(0, num_bin)]
    # group[-1].append(delay_delay_time_tmp[num_bin * len_bin:])
    # group[-1] = flatten(group[-1][:])
    #
    # total = len(delay_delay_time_tmp)
    # total_good = sum(delay_delay_time_tmp)
    # total_bad = total - total_good
    #
    # good_list = [sum(group[i]) for i in range(0, num_bin)]  # number of good for each group
    # bad_list = [len(group[i]) - good_list[i] for i in range(0, num_bin)]  # number of bad for each group
    # good_ks_result_list = [0]  # accumulated freq for good
    # bad_ks_result_list = [0]  # accumulated freq for bad
    #
    # for i in range(1, num_bin + 1):
    #     good_ratio = sum(good_list[:i]) * 1.0 / total_good
    #     bad_ratio = sum(bad_list[:i]) * 1.0 / total_bad
    #     good_ks_result_list.append(good_ratio)
    #     bad_ks_result_list.append(bad_ratio)
