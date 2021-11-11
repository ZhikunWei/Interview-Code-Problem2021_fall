#!/usr/bin/python 
# -*-coding:utf-8 -*-
# ac

roomA = int(input())
roomB = int(input())
N = int(input())
path = {}
for i in range(N):
    a, b = [int(x) for x in input().split()]
    if a not in path:
        path[a] = []
    if b not in path:
        path[b] = []
    path[a].append(b)
    path[b].append(a)
visited = {}

import queue
q1 = queue.Queue()
q1.put(roomA)
q2 = queue.Queue()
res = 0
while True:
    q2 = q1
    q1 = queue.Queue()
    
    while not q2.empty():
        t = q2.get()
        if t == roomB:
            print(res)
            exit()
        visited[t] = 1
        
        for x in path[t]:
            if x not in visited:
                q1.put(x)
    res += 1