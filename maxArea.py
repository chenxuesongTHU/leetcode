#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   maxArea  
@Time        :   2021/3/25 4:15 下午
@Author      :   Xuesong Chen
@Description :   
"""
from typing import List


class Solution_old:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for start_idx in range(0, n - 1):
            for end_idx in range(start_idx + 1, n):
                area = min(height[start_idx], height[end_idx]) * (end_idx - start_idx)
                if area > max_area:
                    max_area = area
        return max_area

# 消去短板，意味着不考虑该短板作为一条边的所有可能的状态，在这些所有可能的状态中，消去前的状态面积最大。

class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height)-1
        l = 0
        max_area = 0
        while l < r:
            area = min(height[r], height[l]) * (r-l)
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area



print(
    Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
)

