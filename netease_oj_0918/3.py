#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

'''
2 3 10
S##
.#G

8

2 3 10
S##
..G

-1
'''

H, W, T = [int(x) for x in input().split()]
mat = []
visited = [[0 for x in  range(W)] for y in range(H) ]
for i in range(H):
    line = input()
    mat.append(line)

mini_stars = H * W
stars = 0

def dfs(x, y):
    global mini_stars, stars, visited
    if mat[x][y] == 'G':
        mini_stars = min(mini_stars, stars)
    if mat[x][y] == '#':
        stars += 1
    visited[x][y] = 1
    for xx, yy, in [(x,y+1), (x+1, y), (x, y-1), (x-1, y)]:
        if xx < 0 or xx >= H or yy < 0 or yy >= W or visited[xx][yy]:
            continue
        dfs(xx, yy)
    if mat[x][y] == '#':
        stars -= 1
    visited[x][y] = 0

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 'S':
            dfs(i, j)
            
print(mini_stars)