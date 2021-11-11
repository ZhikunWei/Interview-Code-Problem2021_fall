#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

n = int(input())
a = input()
a = a.split(' ')
a = [int(ai) for ai in a]
squres = []
i = 0
while i * i < 10e9:
    squres.append(i*i)
    i += 1

def bin_search(x):
    left = 0
    right = i-1
    while left <= right:
        mid = (left + right) // 2
        if squres[mid] < x:
            left = mid
        elif squres[mid] >= x:
            right = mid
        if left + 1 == right or left == right:
            break
    if left + 1 == right:
        return min(x-squres[left], squres[right]-x)
    return 0

nums = []
for ai in a:
    nums.append(bin_search(ai))
sorted_nums = sorted(nums)
res = 0
for i in range(n//2):
    res += sorted_nums[i]
print(res)
