#23.py
#coding: utf-8
import json
import os
import re

def UK(fname):
    uk_list = []
    with open(fname,'r',encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            if data["title"]=="イギリス":
                uk_list.append(data["text"])
    return uk_list

if __name__ == '__main__':
    dirpath = os.path.dirname(__file__)
    fname = os.path.join(dirpath,'jawiki-country.json')
    uk_list = UK(fname)
    pattern_text1 = r'(={2,})\s*(.*?)={2,}'
    pattern1 = re.compile(pattern_text1)
    match = pattern1.findall(uk_list[0])
    for s in match:
        level = len(s[0])-1
        print('{0}:{1}'.format(s[1],level))
