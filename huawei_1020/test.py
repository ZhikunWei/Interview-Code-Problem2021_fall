#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

c = ['ab', 'aab', 'aabc', 'aabbcc', 'abcd']
for item in c:
    d = {}
    for i in range(len(item)):
        if item[i] not in d:
            d[item[i]] = 0
        d[item[i]] += 1
    letter_list = list(d.items())
    cnt = letter_list[0][1]
    is_answer = True
    for i in range(1, len(letter_list)):
        if cnt != letter_list[i][1]:
            is_answer = False
    if is_answer:
        print(item)
        