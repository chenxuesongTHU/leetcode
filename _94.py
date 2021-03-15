#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _94  
@Time        :   2021/3/14 11:02 下午
@Author      :   Xuesong Chen
@Description :    二叉树的中序遍历
"""

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归
    '''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        if root.left != None:
            ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        if root.right != None:
            ret.extend(self.inorderTraversal(root.right))
        return ret
    '''
    # 非递归
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ret = []
        cur = root
        while cur.left != None:
            stack.append(cur)
            cur = root.left


if __name__ == '__main__':
    solution = Solution()
    b = TreeNode(2)
    a = TreeNode(1, b)
    _3 = TreeNode(3)
    _2 = TreeNode(2, _3)
    _1 = TreeNode(1, None, _2)
    # a = TreeNode(1)
    print(
        solution.inorderTraversal(a),
        solution.inorderTraversal(None),
        sep='\n',
    )