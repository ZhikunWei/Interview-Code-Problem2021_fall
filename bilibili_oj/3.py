#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

# ac

data = ''
while True:
    x = input()
    data += x
    if ']]' in x:
        break
data = eval(data)
n = len(data)
m = len(data[0])

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or data[x][y]==0:
        return 0
    # if 0 <= x-1 < n and not visited[x-1][y]:
    #     dfs(x-1, y)
    visited[x][y] = 1
    return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
    
visited = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            visited[i][j] = 1
res = 0
for i in range(n):
    for j in range(m):
        res = max(res, dfs(i, j))
print(res)

