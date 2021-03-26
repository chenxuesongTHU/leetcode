#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   numTrees  
@Time        :   2021/3/18 10:06 下午
@Author      :   Xuesong Chen
@Description :   
"""

class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1)
        G[0] = 1
        G[1] = 1
        # G[2] = 2
        for i in range(2, n+1):
            for j in range(0, i):
                G[i] += G[j]*G[i-j-1]
                # print(f"{j}:{G[j]},{i-j-1}: {G[i-j-1]}")
        return G[n]

print(
    Solution().numTrees(4)
)