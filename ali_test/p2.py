#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

n = int(input())
a = input()
a = [int(ai) for ai in a.split(' ')]
b = input()
b = [int(bi) for bi in b.split(' ')]
print(a)
print(b)
res = 400000
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] >= a[j]:
            continue
        for k in range(j+1, len(a)):
            if a[j] >= a[k]:
                continue
            res = min(res, b[i]+b[j]+b[k])
            print(res, i, j, k)
if res == 400000:
    print(-1)
else:
    print(res)
    