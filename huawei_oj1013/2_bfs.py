#!/usr/bin/python 
# -*-coding:utf-8 -*-
# ac
m, n = [int(x) for x in input().split()]
graph = [['.' for i in range(n)] for j in range(m)]
start = [int(x) for x in input().split()]
end = [int(x) for x in input().split()]
graph[start[0]][start[1]] = 's'
graph[end[0]][end[1]] = 'e'
num = int(input())
for i in range(num):
    x, y = [int(x) for x in input().split()]
    graph[x][y] = '#'
# for x in graph:
#     print(x)
res = {}
visited = [[False for i in range(n)] for j in range(m)]

import queue

q1 = queue.Queue()
q1.put((start[0], start[1], 1))
path_len = 0
finish = False
while not q1.empty():
    q2 = q1
    q1 = queue.Queue()
    layer = {}
    while not q2.empty():
        x, y, cnt = q2.get()
        if graph[x][y] == 'e':
            print(cnt, path_len)
            finish = True
            break
        for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= xx < m and 0 <= yy < n and not visited[xx][yy] and graph[xx][yy] != '#':
                if (xx, yy) not in layer:
                    layer[(xx, yy)] = 0
                layer[(xx, yy)] += cnt
    if finish:
        break
    # print(layer)
    for x, y in layer:
        q1.put((x, y, layer[(x, y)]))
        visited[x][y] = True
    
    path_len += 1
if not finish:
    print(0, 0)