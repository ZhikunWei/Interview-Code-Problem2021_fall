#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

data = [2, 4, 1, 5, 6, 7, 2]
# 最长递增子序列的长度
n = len(data)
dp = []
dp_max_val = []
for i in range(n):
    dp.append(1)
    dp_max_val.append(data[i])
dp[0] = 1
for i in range(n):
    for j in range(i):
        if dp_max_val[i] > dp_max_val[i]:
            dp[i] = dp[j] + 1
            dp_max_val[i] = dp_max_val[j]
