import os
import sys

dirpath = os.path.dirname(__file__)
fname = os.path.join(dirpath,"hightemp.txt")
count=0
first=True
list =[]
with open(fname,"r",encoding="utf-8") as datas:
    list_data = [data.split("\t")[0] for data in datas]
    list_data.sort()
    for name in list_data:
        if first:
            first=False
            name_p = name
            count=1
            continue
        if name_p!=name:
            list.append([name_p,count])
            name_p=name
            count=1
        else:
            count+=1
    list.append([name_p,count])
list.sort(key=lambda x:x[1],reverse=True)
for result in list:
    print(result[0],result[1])
