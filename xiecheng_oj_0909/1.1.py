#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
n, m, k = [int(x) for x in input().split()]
mat = []
for i in range(n):
    line = [int(x) for x in input().split()]
    mat.append(line)
import numpy as np
mat = np.array(mat)
res = 0
mat_sum = np.zeros_like(mat)
for i in range(n):
    for j in range(m):
        if i > 0:
            mat_sum[i, j] += mat_sum[i-1, j]
        if j > 0:
            mat_sum[i, j] += mat_sum[i, j-1]
        if i > 0 and j > 0:
            mat_sum[i, j] -= mat_sum[i-1, j-1]
        mat_sum[i, j] += mat[i, j]

res = 0
for i in range(n-k+1):
    for j in range(m-k+1):
        cur = mat_sum[i+k-1, j+k-1]
        if i > 0:
            cur -= mat_sum[i-1, j+k-1]
        if j > 0:
            cur -= mat_sum[i+k-1, j-1]
        if i > 0 and j > 0:
            cur += mat_sum[i-1, j-1]
        
        res = max(res, cur)
    
print(res)