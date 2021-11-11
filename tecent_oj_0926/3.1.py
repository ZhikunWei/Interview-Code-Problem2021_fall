#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

# baoli

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

mean_val = sum(a[:k])/k
max_val = max([mean_val] + a[k:])
min_val = min([mean_val] + a[k:])
res = max_val - min_val
for i in range(k, n):
    mean_val = sum(a[i-k+1:i+1])/k
    max_val = max([mean_val]+a[:i-k+1]+ a[i+1:])
    min_val = min([mean_val]+a[:i-k+1]+ a[i+1:])
    res = min(max_val-min_val, res)
print(res)
