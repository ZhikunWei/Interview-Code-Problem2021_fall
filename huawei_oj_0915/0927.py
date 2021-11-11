#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

d = {'2':'abc', '3':'def'}

data = '2333'
res = ['']
for x in data:
    cur = []
    for t in d[x]:
        for val in res:
            cur.append(val+t)
    res = cur
print(res)