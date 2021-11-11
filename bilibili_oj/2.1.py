#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

# ac

res = 0
c = int(input())


def dfs(node):
    global res, relation, visited
    if visited[node]:
        return 0
    visited[node] = 1
    for k in relation[node]:
        if not visited[k]:
            dfs(k)
    return 0


for _ in range(c):
    n, m = [int(x) for x in input().split()]
    relation = {}
    for i in range(n):
        relation[i] = [i]
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        relation[a].append(b)
        relation[b].append(a)
    
    visited = [0] * n
    res = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            res += 1
    print(res)

