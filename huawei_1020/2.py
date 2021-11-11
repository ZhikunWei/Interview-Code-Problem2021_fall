#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
out =    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

def requeue(people):
    people = sorted(people, key=lambda x:x[0], reverse=True)
    res = []
    idx = 0
    while idx < len(people):
        cur_people = []
        while idx+1 < len(people) and people[idx][0] == people[idx+1][0]:
            cur_people.append(people[idx])
            idx += 1
        cur_people.append(people[idx])

        cur_people = sorted(cur_people, key=lambda x: x[1])
        for p in cur_people:
            res = res[:p[1]] + [p] + res[p[1]:]
        idx += 1
    print(res)

requeue(people)
    
