from os import listdir
from os.path import isfile, join
import ast
import os
#
DIR_NAME = './data'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#
# print(onlyfiles)
#
# for i in onlyfiles:
#     with open(i, 'r') as f:
#         print(f)
res1 = {}
res2 = {}
res3 = {}

for file in os.listdir(DIR_NAME):
    if (file.endswith('.out')):
        f = open(os.path.join(DIR_NAME, file))
        lines = f.readlines()
        dic1 = ast.literal_eval(lines[16])
        dic2 = ast.literal_eval(lines[18])
        dic3 = ast.literal_eval(lines[20])
        for key in dic1:
            if key in res1:
                res1[key] = [(dic1[key][0] * dic1[key][1] + res1[key][0] * res1[key][1]) / (dic1[key][1] + res1[key][1]), dic1[key][1] + res1[key][1]]
            else:
                res1[key] = [dic1[key][0], dic1[key][1]]

        for key in dic2:
            if key in res2:
                res2[key] = [(dic2[key][0] * dic2[key][1] + res2[key][0] * res2[key][1]) / (dic2[key][1] + res2[key][1]), dic2[key][1] + res2[key][1]]
            else:
                res2[key] = [dic2[key][0], dic2[key][1]]

        for key in dic3:
            if key in res3:
                res3[key] = [(dic3[key][0] * dic3[key][1] + res3[key][0] * res3[key][1]) / (dic3[key][1] + res3[key][1]), dic3[key][1] + res3[key][1]]
            else:
                res3[key] = [dic3[key][0], dic3[key][1]]
