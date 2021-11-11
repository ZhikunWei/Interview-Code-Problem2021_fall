#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = []
        for i in range(numRows):
            res.append([])
        index = 0
        pos = 0
        while index < len(s):
            if pos // numRows  % (numRows-1) == 0:
                res[pos%numRows].append(s[index])
                index += 1
            else:
                if pos // numRows % (numRows-1) + pos % numRows == numRows-1:
                    res[pos % numRows].append(s[index])
                    index += 1
                else:
                    res[pos % numRows].append('')
            pos += 1
        out = ''
        
        for x in res:
            out += ''.join(x)
        return out

c = Solution()
print(c.convert( "PAYPALISHIRING", 3))
        
        