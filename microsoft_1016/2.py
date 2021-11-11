#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

def solution(A, B, C):
    # write your code in Python 3.6
    a, b, c = sorted([(A,'a'), (B,'b'), (C,'c')], key=lambda x:x[0], reverse=True)
    result = [''] * 310
    for i in range(a[0]):
        if i % 2 == 0:
            result[i*3] = a[1]
        else:
            result[(i-1)*3+1] = a[1]
    for i in range(b[0]):
        if i <= a[0]//2:
            result[i*6+2] = b[1]
        else:
            result[(i-a[0]//2-1)*6+3] = b[1]
    for i in range(b[0], b[0]+c[0]):
        if i <= a[0]//2:
            result[i*6+2] = c[1]
        else:
            result[(i-a[0]//2-1)*6+3] = c[1]
        # if i % 2 == 0:
        #     result[i*3+4] = c[1]
        # else:
        #     result[(i-1)*3+5] = c[1]
    result = ''.join(result)
    cur_letter = a[1]
    cur_cnt = 1
    # print(result)
    for i in range(1, len(result)):
        if cur_letter == result[i]:
            cur_cnt += 1
            if cur_cnt >= 3:
                return result[:i]
        else:
            cur_letter = result[i]
            cur_cnt = 1
    return result

print(solution(3, 30, 3))