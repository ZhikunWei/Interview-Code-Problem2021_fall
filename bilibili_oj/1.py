#!/usr/bin/python 
# -*-coding:utf-8 -*-


__author__ = '99K'
n, first, second = [int(x) for x in input().split()]
players = []
for i in range(1, n+1):
    players.append(i)
import queue
q1 = queue.Queue()
q2 = queue.Queue()
res_min = 0
res_max = 6
q1.put(players)
while not q1.empty():
    q1, q2 = q2, q1
    while not q2.empty():
        cur = q2.get()
        children = []

        for i in range(2 ** (len(cur)//2)):
            for j in range(len(cur)//2):
                pass
            
            

