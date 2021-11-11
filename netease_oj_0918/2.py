#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

# ac

T = int(input())
for _ in range(T):
    A, B, C, x, y, z = [int(x) for x in input().split()]
    
    # BAC
    res1 = -1
    if min(B - 1, A) > 1:
        res1 = x * max(0, A - B + 1) + z * max(0, C - min(B - 1, A) + 1)
    
    # BCA
    res2 = -1
    if min(B - 1, C) > 1:
        res2 = z * max(0, C - B + 1) + x * max(0, A - min(B - 1, C) + 1)
    
    # ACB
    res3 = -1
    if min(A - 1, C) > 1:
        res3 = z * max(0, C - A + 1) + y * max(0, B - min(A - 1, C) + 1)
    
    # CAB
    res4 = -1
    if min(C - 1, A) > 1:
        res4 = x * max(0, A - C + 1) + y * max(0, B - min(C - 1, A) + 1)
    
    res = max(res1, res2, res3, res4)
    # print(res, res1, res2, res3, res4)
    for val in (res1, res2, res3, res4):
        if val != -1 and val < res:
            res = val
    
    print(res)
