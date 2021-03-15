#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _ListNode  
@Time        :   2021/3/15 12:56 下午
@Author      :   Xuesong Chen
@Description :   
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        res = []
        while pHead != None:
            res.append(pHead.val)
            pHead = pHead.next

        return reversed(res)

if __name__ == '__main__':
    solution = Solution()
    print(
        solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
        solution.searchMatrix([[1, 3, 5, 7], [10, 11, 13, 20], [23, 30, 34, 60]], 13),
        solution.searchMatrix([[1, 3, 5, 7], [10, 11, 13, 20], [23, 30, 34, 60]], 16),
    )