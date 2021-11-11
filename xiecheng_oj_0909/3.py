#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
n, root = [int(x) for x in input().split()]
colors =[0] + [int(x) for x in input().split()]
edges = {}
for i in range(n-1):
    x, y = [int(k) for k in input().split()]
    if x not in edges:
        edges[x] = []
    edges[x].append(y)
uniq_sums = {}

def cal_sum(root):
    s = 0
    if root not in edges:
        uniq_sums[root] = 0
        return 0
    for node in edges[root]:
        s += cal_sum(node)
        if colors[root] != colors[node]:
            s += 1
    uniq_sums[root] = s
    return s

cal_sum(root)

for i in range(1, n+1):
    print(uniq_sums[i], end=' ')