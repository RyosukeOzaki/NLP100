import os
import sys

dirpath = os.path.dirname(__file__)
fname = os.path.join(dirpath,"hightemp.txt")

list_data = list()
with open(fname,"r",encoding="utf-8") as datas:
    for data in datas:
        col = data.split("\t")
        col = data.strip()
        list_data.append(col)
list_data.sort(key=lambda x:x[2])
for line in list_data:
    print(line)
