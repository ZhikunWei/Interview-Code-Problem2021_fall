#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


password = 'weizhikun'
sum_of_digit = sum([ord(x) - ord('a') for x in password]) % 1000
sep = ',.?!@#_'[sum_of_digit % len(',.?!@#_')]
final_pass = password + sep + '{:03d}'.format(sum_of_digit)
print(final_pass)  # weizhikun#117