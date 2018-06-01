import csv
import os
dirpath = os.path.dirname(__file__)
filepath_cat = os.path.join(dirpath, 'cat.txt')
filepath_col1 = os.path.join(dirpath, 'col1.txt')
filepath_col2 = os.path.join(dirpath, 'col2.txt')
list1 = list()
with open(filepath_col1, 'r', encoding='utf-8',) as fc1:
    with open(filepath_col1, 'r', encoding='utf-8') as fc2:
        with open(filepath_cat,'w',encoding='utf-8') as fw:
            for col1,col2 in zip(fc1,fc2):
                list1 = col1.split()
                list2 = col2.split()
            for col1,col2 in zip(list1,list2):
                fw.write(col1+"  "+col2+"\n")
