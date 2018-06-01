import os
import sys
import math

dirpath = os.path.dirname(__file__)
filename = os.path.join(dirpath,"hightemp.txt")

args = sys.argv
list_data = []
num_list = range(int(args[1]))
count = int(args[1])
with open(filename,"rt",encoding="utf-8") as datas:
    for data in datas:
        list_data.append(data)
    for line in list_data:
        if count==int(args[1]):
            count=0
        filename2 = os.path.join(dirpath,"split{0}.txt".format(count))
        with open(filename2,"a",encoding="utf-8") as fw:
            fw.write(str(line))
            count+=1
