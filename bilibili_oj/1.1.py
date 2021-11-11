#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

n, first, second = [int(x) for x in input().split()]
if n <= 2:
    print(1, 1)
elif n == 3:
    if first + second ==4:
        print(1, 1)
    else:
        print(2, 2)
elif n <= 8:
    print(1, 3)
elif n <= 16:
    print(2, 4)
else:
    print(2, 5)