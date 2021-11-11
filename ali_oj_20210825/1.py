#!/usr/bin/python 
# -*-coding:utf-8 -*-

n = int(input())
nums = [int(x) for x in input().split()]
res = 0
for i in range(1, n-1):
    if min(nums[i-1],nums[i+1]) < nums[i] < max(nums[i-1],nums[i+1]):
        res += 1
print(res)
