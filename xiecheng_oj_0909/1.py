#!/usr/bin/python 
# -*-coding:utf-8 -*-
n, m, k = [int(x) for x in input().split()]
mat = []
for i in range(n):
    line = [int(x) for x in input().split()]
    mat.append(line)
import numpy as np
mat = np.array(mat)
res = 0
for i in range(n):
    line = []
    for ii in range(m):
        line.append(sum(mat[i:i+k, ii]))
    line = np.array(line)
    dp = []
    for ii in range(k - 1):
        dp.append(0)
    dp.append(sum(line[:k]))
    res = max(res, dp[-1])
    for ii in range(k, m):
        dp.append(dp[-1] + line[ii] - line[ii - k])
        res = max(res, dp[-1])
    
    for j in range(i+k, n):
        for ii in range(m):
            line[ii] += (mat[j, ii] - mat[j-k, ii])
        dp = []
        for ii in range(k-1):
            dp.append(0)
        dp.append(sum(line[:k]))
        res = max(res, dp[-1])
        for ii in range(k, m):
            dp.append(dp[-1]+line[ii] - line[ii-k])
            res = max(res, dp[-1])
print(res)