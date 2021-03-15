#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _editdistance  
@Time        :   2021/3/15 8:27 下午
@Author      :   Xuesong Chen
@Description :   
"""
from pprint import pprint as print

def edit_distance(str1, str2):
    n_1 = len(str1)
    n_2 = len(str2)
    edit = [[0] * (n_1+1) for i in range(n_2+1) ]
    for i in range(len(str1) + 1):
        edit[0][i] = i
    for i in range(len(str2) + 1):
        edit[i][0] = i
    for _idx2 in range(1, n_2 + 1):
        for _idx1 in range(1, n_1+1):
            if str1[_idx1-1] == str2[_idx2-1]:
                edit[_idx2][_idx1] = edit[_idx2-1][_idx1-1]
            else:
                edit[_idx2][_idx1] = min(
                    edit[_idx2 - 1][_idx1],
                    edit[_idx2][_idx1 - 1],
                    edit[_idx2 - 1][_idx1 - 1],
                ) + 1
    print(edit)
if __name__ == '__main__':
    edit_distance('jarrry', 'jerr')