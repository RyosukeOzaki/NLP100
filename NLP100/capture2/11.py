import csv
import os
dirpath = os.path.dirname(__file__)
filepath = os.path.join(dirpath, 'hightemp.txt')
filepath_col1 = os.path.join(dirpath, 'col1.txt')
filepath_col2 = os.path.join(dirpath, 'col2.txt')
list1 = list()
with open(filepath, 'r', encoding='utf-8') as fr:
    fw1 = open(filepath_col1, 'w', encoding='utf-8')
    fw2 = open(filepath_col2, 'w', encoding='utf-8')
    reader = csv.reader(fr, delimiter='\t')
    for row in reader:
        fw1.write(row[0]+'  ')
        fw2.write(row[1]+'  ')
