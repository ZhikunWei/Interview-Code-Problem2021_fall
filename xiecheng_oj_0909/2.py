#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
import queue
q = queue.PriorityQueue()
n = int(input())
for _ in range(n):
    line = [int(x) for x in input().split()]
    if line[0] == 1:
        x, y = line[1], line[2]
        for i in range(x):
            q.put((y, 1))
        
        pass
    elif line[0] == 2:
        x = line[1]
        if x > q.qsize():
            print('no')
        else:
            for i in range(x):
                q.get()
            print('yes')
    elif line[0] == 3:
        tq = queue.PriorityQueue()
        while not q.empty():
            y, _ = q.get()
            y -= 1
            if y > 0:
                tq.put((y, 1))
        q = tq
    elif line[0] == 4:
        if q.empty():
            print(0)
        else:
            y, _ = q.get()
            print(y)
            q.put((y, 1))