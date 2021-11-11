#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

T = int(input())
for _ in range(T):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    x, y, z, w = 0, 0, 0, 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                x += b[i] == b[j]
                y += b[i] != b[j]
            else:
                z += b[i] == b[j]
                w += b[i] != b[j]
    ei = (x+w)/(x+y+z+w)
    print(ei)

