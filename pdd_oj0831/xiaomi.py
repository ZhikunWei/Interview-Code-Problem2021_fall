#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def conv2d(self, kernel, image, stride):
        import numpy as np
        # Write Code Here
        kernel_size, kernel_data = kernel.split(',')
        kernel_size = [int(x) for x in kernel_size.split()]
        kernel_data = [int(x) for x in kernel_data.split()]
        kernel_squre = np.array(kernel_data).reshape(kernel_size)
        
        image_size, image_data = image.split(',')
        image_size = [int(x) for x in image_size.split()]
        image_data = [int(x) for x in image_data.split()]
        padded = []
        index = 0
        
        for i in range(image_size[0] + kernel_size[0] // 2 + kernel_size[0] // 2):
            t = []
            for j in range(image_size[1] + kernel_size[1] // 2 + kernel_size[1] // 2):
                if kernel_size[0] // 2 <= i < image_size[0] + kernel_size[0] // 2 and kernel_size[1] // 2 <= j < \
                        image_size[1] + kernel_size[1] // 2:
                    t.append(image_data[index])
                    index += 1
                else:
                    t.append(0)
            padded.append(t)
        padded = np.array(padded)
        print(padded)
        print(kernel_squre)
        res = []
        for i in range(0, image_size[0] + kernel_size[0] // 2 + kernel_size[0] // 2 - kernel_size[0] + 1, stride):
            t = []
            for j in range(0, image_size[1] + kernel_size[1] // 2 + kernel_size[1] // 2 - kernel_size[1] + 1, stride):
                s = 0
                for ii in range(kernel_size[0]):
                    for jj in range(kernel_size[1]):
                        s += padded[i + ii][j + jj] * kernel_squre[ii][jj]
                t.append(s)
            res.append(t)
        print(res)
        res_vec = []
        for x in res:
            for y in x:
                res_vec.append(str(int(y)))
        res_str = '%d %d, ' % (len(res), len(res[0]))
        res_str += ' '.join(res_vec)
        return res_str


try:
    _kernel = input()
except:
    _kernel = None

try:
    _image = input()
except:
    _image = None

_stride = int(input())

s = Solution()
res = s.conv2d(_kernel, _image, _stride)

print(res + "\n")

t = '''
5 5, 1 1 1 1 1 1 2 2 2 1 1 2 4 2 1 1 2 2 2 1 1 1 1 1 1
5 5, 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2
'''