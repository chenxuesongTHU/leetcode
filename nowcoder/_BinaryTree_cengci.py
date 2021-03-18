#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _BinaryTree_cengci  
@Time        :   2021/3/15 11:14 下午
@Author      :   Xuesong Chen
@Description :   
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self , root):
        # write code here
        cur_layer = [root]
        next_layer = []
        res = []
        if root is None:
            return res
        while True:
            _v_l = []
            for node in cur_layer:
                if node is None:
                    continue
                _v_l.append(node.val)
                next_layer += [node.left, node.right]
            cur_layer = next_layer
            next_layer = []
            res.append(_v_l)
            if all(node is None for node in cur_layer):
                break

        return res

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
        solution.levelOrder(b),
        solution.levelOrder(_1),
    )