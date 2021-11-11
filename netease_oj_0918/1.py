#!/usr/bin/python 
# -*-coding:utf-8 -*-

# ac
N = int(input())
mat = []
for i in range(N):
    line = [int(x) for x in input().split()]
    mat.append(line)

while len(mat) > 1:
    new_mat = []
    for i in range(len(mat)//2):
        new_line = []
        for j in range(len(mat[0])//2):
            vals = [mat[i*2][j*2], mat[i*2+1][j*2], mat[i*2][j*2+1], mat[i*2+1][j*2+1]]
            num = sorted(vals)[-2]
            new_line.append(num)
        new_mat.append(new_line)
    mat = new_mat
print(mat[0][0])

