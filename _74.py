#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _74  
@Time        :   2021/3/14 9:00 下午
@Author      :   Xuesong Chen
@Description :   搜索二维矩阵
                2D -> 1D binary search
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        _1d_list = []
        d = len(matrix)
        for i in range(d):
            _1d_list.extend(matrix[i])

        # 二分查找
        mid_idx = int((len(_1d_list)-1) / 2)
        left = 0
        right = len(_1d_list)-1
        while _1d_list[mid_idx] != target:
            if target < _1d_list[mid_idx]:
                right = mid_idx - 1
                mid_idx = int((left + right)/2)
            elif target > _1d_list[mid_idx]:
                left = mid_idx + 1
                mid_idx = int((left + right)/2)
            else:
                return True
            if left > right:
                return False
            # if left == right:
            #     if _1d_list[right] == target or _1d_list[left] == target:
            #         return True
            #     else:
            #         return False


        return True

if __name__ == '__main__':
    solution = Solution()
    print(
        solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),
        solution.searchMatrix([[1,3,5,7],[10,11,13,20],[23,30,34,60]], 13),
        solution.searchMatrix([[1,3,5,7],[10,11,13,20],[23,30,34,60]], 16),
        solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11),
        solution.searchMatrix([[1, 3, 5]], 1),
        solution.searchMatrix([[1]], 0),
        solution.searchMatrix([[1]], 1),
        sep='\n',
    )