#!/usr/bin/python 
# -*-coding:utf-8 -*-
# TLE 90%
m, n = [int(x) for x in input().split()]
graph = [['.' for i in range(n)] for j in range(m)]
start = [int(x) for x in input().split()]
end = [int(x) for x in input().split()]
graph[start[0]][start[1]] = 'start'
graph[end[0]][end[1]] = 'end'
num = int(input())
for i in range(num):
    x, y = [int(x) for x in input().split()]
    graph[x][y] = '#'

res = {}
visited = [[False for i in range(n)] for j in range(m)]


def dfs(x, y, path_len):
    if graph[x][y] == 'end':
        if path_len not in res:
            res[path_len] = 0
        res[path_len] += 1
        return
    visited[x][y] = True
    if x-1 >= 0 and not visited[x-1][y] and graph[x-1][y] != '#':
        dfs(x-1, y, path_len+1)
    if y-1 >= 0 and not visited[x][y-1] and graph[x][y-1] != '#':
        dfs(x, y-1, path_len+1)
    if x+1<m and not visited[x+1][y] and graph[x+1][y] != '#':
        dfs(x + 1, y, path_len + 1)
    if y+1 < n and not visited[x][y+1] and graph[x][y+1] != '#':
        dfs(x, y+1, path_len+1)
    visited[x][y] = False

dfs(start[0], start[1], 0)
res = sorted(res.items(), key=lambda x: x[0])
if len(res) == 0:
    print(0, 0)
else:
    print(res[0][1], res[0][0])