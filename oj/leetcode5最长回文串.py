#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


def longestPalindrome(s: str) -> str:
    h = [ [False for i in range(len(s))] for j in range(len(s)) ]
    index_i = 0
    max_len = 1
    for i in range(len(s)):
        h[i][i] = True
        if i - 1 >= 0:
            h[i - 1][i] = s[i] == s[i - 1]
            if h[i - 1][i]:
                index_i = i - 1
                max_len = 2
    for length in range(3, len(s) + 1):
        for i in range(len(s) - length + 1):
            j = i + length - 1
            h[i][j] = h[i + 1][j - 1] and (s[i] == s[j])
            if h[i][j] and length > max_len:
                max_len = length
                index_i = i
    return s[index_i: index_i + max_len]

print(longestPalindrome("babad"))