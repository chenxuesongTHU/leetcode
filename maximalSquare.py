#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   maximalSquare  
@Time        :   2021/3/25 10:39 上午
@Author      :   Xuesong Chen
@Description :   
"""
from pprint import pprint as print
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n_row = len(matrix)
        n_col = len(matrix[0])
        dp = [[0] * (n_col + 1) for i in range(n_row + 1)]
        max_edge = 0
        for i in range(n_row):
            for j in range(n_col):
                if matrix[i][j] == '1':
                    current_edge = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
                    dp[i + 1][j + 1] = current_edge
                    if current_edge > max_edge:
                        max_edge = current_edge
        # print(dp)
        # print(max_squ)
        return max_edge * max_edge


print(
    Solution().maximalSquare(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "1"]
        ]
    )
)
