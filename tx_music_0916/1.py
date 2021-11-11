#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


class Solution:
    def minM(self, n, k):
        #cache = [0]
        cache = {0:0}
        res = 0
        i = 1
        while True:
            t = i
            cur = 0
            if t % k == 1:
                cur += 1
            cur += cache[t // k]
            cache[t] = cur
            if t >= k*k and t // k // k in cache:
                del cache[t//k//k]
            #cache.append(cur)
            res += cur
            # print('\nres = ', res, ', i = ', i)
            if res >= n:
                break
            i += 1
        return i

s = Solution()
print(s.minM(10000000,10))