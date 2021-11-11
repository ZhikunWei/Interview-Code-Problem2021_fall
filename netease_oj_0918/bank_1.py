#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

T = int(input())
for _ in range(T):
    A, B, C = [int(x) for x in input().split()]
    res = 0
    if -A < 0:
        res = 0
    elif A == 0:
        res = 1
    elif -A > 0:
        res = 2
    
    if A-B < 0:
        res *= 0
    elif A-B==0:
        res *= 1
    elif A-B > 0:
        res *= 2
    
    if -C-A*A*(A-B) < 0:
        res *= 0
    elif -C-A*A*(A-B) == 0:
        res *=1
    elif -C-A*A*(A-B) > 0:
        res *= 2
        