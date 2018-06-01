import os
import sys
dirpath = os.path.dirname(__file__)
filepath = os.path.join(dirpath, 'hightemp.txt')

args = sys.argv
n = int(args[1])
list1 = list()
with open(filepath,"r",encoding="utf-8") as fr:
    for line in fr:
        list1.append(line)
    for l in list1[-n:]:
        print(l)
