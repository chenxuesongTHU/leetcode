#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   zuidazheng  
@Time        :   2021/3/19 7:38 下午
@Author      :   Xuesong Chen
@Description :   
"""
# coding=utf-8
import sys
# str = input()
# print(str)
import numpy as np

matrix = np.array([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
])
n_r = len(matrix)
n_c = len(matrix[0])
_max = min(n_r, n_c)
max_v = 1

print(matrix[0:2,0:2])

for i in range(_max):
    for j in range(_max):
        if matrix[i][j] == '0':
            continue
        print(matrix[0:2][0:2])
        for k in range(1, _max):
            if k > max_v:
                max_v = k
            if i+k > n_r-1 or j+k>n_c-1:
                break
            if matrix[i+k][j+k] == '0':
                break

print(max_v)
