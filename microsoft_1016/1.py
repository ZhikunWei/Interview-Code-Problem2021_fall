#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

def solution(riddle):
    # write your code in Python 3.6
    letter_pool = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    def replace(pre, post):
        for i in range(len(letter_pool)):
            if letter_pool[i] != pre and letter_pool[i] != post:
                return letter_pool[i]
    for i in range(len(riddle)):
        if riddle[i] == '?':
            pre = '?' if i - 1 < 0 else res[-1]
            post = '?' if i + 1 > len(riddle)-1 else riddle[i+1]
            candidate = replace(pre, post)
            res.append(candidate)
        else:
            res.append(riddle[i])
    
    return ''.join(res)

print(solution('ab???a???'))