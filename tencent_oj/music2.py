#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


def f(s, k):
    res = 0
    for i in range(len(s)-k):
        res = max(int(s[i:i+k]), res)
    return res



print(f('321', 2))

