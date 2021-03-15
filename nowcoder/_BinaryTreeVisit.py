#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _BinaryTreeVisit  
@Time        :   2021/3/15 10:21 下午
@Author      :   Xuesong Chen
@Description :   
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:

    def threeOrders(self, root):
    # write code here
        self.root = root
        self.first_res = []
        self.middle_res = []
        self.last_res = []
        self.first(root)
        self.middle(root)
        self.last(root)

        return [self.first_res, self.middle_res, self.last_res]

    def first(self, node):
        if node == None:
            return
        self.first_res.append(node.val)
        self.first(node.left)
        self.first(node.right)

    def middle(self, node):
        if node == None:
            return
        self.middle(node.left)
        self.middle_res.append(node.val)
        self.middle(node.right)

        pass
    def last(self, node):
        if node == None:
            return
        self.last(node.left)
        self.last(node.right)
        self.last_res.append(node.val)
        pass

if __name__ == '__main__':
    solution = Solution()
    b = TreeNode(2)
    a = TreeNode(1)
    a.left = b
    _3 = TreeNode(3)
    _2 = TreeNode(2)
    # _2.left = _3
    _1 = TreeNode(1)
    _1.left = _2
    _1.right = _3
    print(
        solution.threeOrders(b)
    )