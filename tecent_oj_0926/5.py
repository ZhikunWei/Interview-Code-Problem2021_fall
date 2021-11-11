#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

e = [1,2,3,5,6,2,1,3,4]
n = 2
rec = {}
for x in e:
    if x not in rec:
        rec[x] = 0
    rec[x] += 1
d = sorted(rec.items(), key=lambda x:x[1], reverse=True)

for ele, cnt in d[:n]:
    print(ele, cnt)
    
    