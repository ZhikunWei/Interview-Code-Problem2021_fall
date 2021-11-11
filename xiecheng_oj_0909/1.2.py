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
for i in range(n-k+1):
    for j in range(m-k+1):
        res = max(res, np.sum(mat[i:i+k, j:j+k]))
print(res)