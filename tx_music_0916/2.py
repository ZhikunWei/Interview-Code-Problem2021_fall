#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

# ac
class Solution:
    def maxLexicographical(self , num ):
        nums = []
        for x in num:
            nums.append(x)
        # write code here
        start = False
        end = False
        for i in range(len(nums)):
            if nums[i] == '0' and not start:
                start = True
            if nums[i] == '1' and start:
                end = True
                break
            if start and not end:
                nums[i] = '1'
        return ''.join(nums)

s = Solution()
print(s.maxLexicographical('01001'))