#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


class Solution:
    def solveNQueens(self, n: int):
        self.res = []
        pos = []
        cols = set()
        dig1 = set()
        dig2 = set()
        self.check_val(n, pos, cols, dig1, dig2)
        return self.res
    
    def check_val(self, n, pos, cols, dig1, dig2):
        print(pos, cols, dig1, dig2)
        if len(pos) == n:
            m = []
            for x in pos:
                t = '.' * x + 'Q' + '.' * (n - 1 - x)
                m.append(t)
            self.res.append(m)
        
        elif len(pos) < n:
            cur_len = len(pos)
            for i in range(n):
                if i not in cols and (cur_len + i) not in dig1 and (cur_len - i) not in dig2:
                    pos.append(i)
                    cols.add(i)
                    dig1.add(cur_len+ i)
                    dig2.add(cur_len - i)
                    self.check_val(n, pos, cols, dig1, dig2)
                    cols.remove(i)
                    dig1.remove(cur_len + i)
                    dig2.remove(cur_len - i)
                    pos.pop(-1)
                
                    
s = Solution()
print(s.solveNQueens(4))