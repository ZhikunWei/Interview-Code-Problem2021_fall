#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

n = int(input())
nums = [int(x) for x in input().split()]
nums = sorted(nums)

if n % 2 == 1:
    mid = (n-1)//2
    res1 = 2 * sum(nums[mid+2:]) + sum(nums[mid:mid+2]) -2 * sum(nums[:mid])
    res2 = 2 * sum(nums[mid+1:]) - sum(nums[mid-1:mid+1]) - 2 * sum(nums[:mid-1])
    print(max(res1, res2))
else:
    mid = n // 2 -1
    res = 2 * sum(nums[mid+2:]) - nums[mid] + nums[mid+1] - 2 * sum(nums[:mid])
    print(res)