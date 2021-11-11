#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
def func(a, b):
    
    if a <= 0 or b <= 0:
        print(a, b, 1)
        return 1
    
    if a%2 != b %2:
        return func(a-1, b) + func(a, b-1)
    else:
        return func(a-1, b) *2

print(func(3, 4))