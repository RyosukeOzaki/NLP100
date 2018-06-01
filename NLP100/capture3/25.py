#25.py
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
    print(uk_list[0])
    print(uk_list[0])
    pattern_text = r'\|(.+?) = (.*)'
    pattern = re.compile(pattern_text)
    match = pattern.findall(uk_list[0])
    for result in match:
        print(result)
