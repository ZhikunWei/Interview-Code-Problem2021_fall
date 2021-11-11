#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import sys
psg1 = []
user_set = set()
for line in sys.stdin:
    if line == '\n':
        break
    a = line.strip().split(',')
    psg1.append([a[0], int(a[1]), int(a[2])])

psg = sorted(psg1, key=lambda x: x[2])
print(psg1)
print(psg)
res = [psg[0]]
user_set.add(psg[0][0])
for i in range(1, len(psg)):
    if res[-1][2] > psg[i][1]:
        continue
    else:
        res.append(psg[i])
        user_set.add(psg[i][0])

for p in psg1:
    if p[0] in user_set:
        print(p[0], end=' ')