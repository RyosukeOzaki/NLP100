import os
import sys
dirpath = os.path.dirname(__file__)
filename = os.path.join(dirpath,"hightemp.txt")
with open(filename,"r",encoding="utf-8") as data_file:
    set_name = set()
    for line in data_file:
        cols = line.split('\t')
        set_name.add(cols[0])
for ken in set_name:
    print(ken)
