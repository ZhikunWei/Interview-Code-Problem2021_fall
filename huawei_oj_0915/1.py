#!/usr/bin/python 
# -*-coding:utf-8 -*-

N = int(input())
pos = []
if N > 0:
    pos = [int(x) for x in input().split()]
M = int(input())
pos = [0] + pos + [10001]
if M >= N:
    res = 10000
else:
    res = pos[1]-pos[0]-1
for i in range(max(0, N-M+1)):
    index = i + 1
    res = max(res, pos[index+M]-pos[index-1]-1)
print(res)
