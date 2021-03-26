#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   NodeTree  
@Time        :   2021/3/18 1:53 下午
@Author      :   Xuesong Chen
@Description :   TODO
"""

class nodeTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


_list = [1, 2, 5, 3, 4, 6, 7]
# _list = sorted(_list)
#  满二叉树
n = len(_list)
node_dic = {}
for idx, v in enumerate(_list):
    node_dic[idx] = nodeTree(v)

for i in range(n//2, -1, -1):
    left_idx = 2*i + 1
    right_idx = 2*i + 2
    if left_idx < n:
        node_dic[i].left = node_dic[left_idx]
    if right_idx < n:
        node_dic[i].right = node_dic[right_idx]

print(node_dic[0])

def pre_order(root):

    stack = []
    res = []
    while root or stack:
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        cur = stack.pop()
        root = cur.right
    return res

def mid_oder(root):

    stack = []
    res = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        cur = stack.pop()
        res.append(cur.val)
        root = cur.right
    return res

def post_order(root):
    # 左 右 根
    stack = []
    res = []
    while stack or root:
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.right

        cur = stack.pop()
        root = cur.left

    return res[::-1]

print(pre_order(node_dic[0]))
print(mid_oder(node_dic[0]))
print(post_order(node_dic[0]))
