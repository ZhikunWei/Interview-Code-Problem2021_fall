#!/usr/bin/python 
# -*-coding:utf-8 -*-

def compute(content="AABB"):
    import math
    d = {}
    s = 0
    for x in set(content):
        cnt = content.count(x)
        d[x] = cnt
        s += cnt
    res = 0
    for k in d:
        res += d[k]/s * math.log2(d[k]/s)
    return res

print(compute())

    