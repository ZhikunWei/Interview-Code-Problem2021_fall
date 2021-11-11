#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

data = 'abcd'
x = 'aaazzz'
y = 'dcba'
z = 'zzzayybbaa' # -> zzzaaabbyy -> zzzbaaabyy


def revert(x):
    last_idx = len(x)-1
    while last_idx-1 >= 0 and x[last_idx] <= x[last_idx-1]:
        last_idx -= 1
    if last_idx == 0:
        return -1
    last_part = sorted(x[last_idx:])
    pre = x[last_idx-1]
    exchange_idx = 0
    while exchange_idx < len(last_part) and last_part[exchange_idx] <= pre:
        exchange_idx += 1
    letter_to_change = last_part[exchange_idx]
    last_part[exchange_idx] = pre
    return x[:last_idx-1] + letter_to_change + ''.join(last_part)

print(revert(data))
print(revert(x))
print(revert(y))
print(revert(z))