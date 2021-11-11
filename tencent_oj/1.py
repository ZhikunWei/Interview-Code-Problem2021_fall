#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
n, m = [int(x) for x in input().split()]
times = []
for i in range(n):
    times.append([int(x) for x in input().split()])
total_time = 0.0
locks = []
for i in range(m):
    key = []
    for j in range(n):
        key.append(times[j][i])
    key = sorted(key)
    for j in range(n):
        total_time += (n-j)/n*key[j]
print(total_time)