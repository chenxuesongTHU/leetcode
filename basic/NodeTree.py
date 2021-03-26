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


_list = [45, 12, 32, 4, 6, 2]
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

def midOrder(root):
    res = []
    stack = []
    p = root
    while p or stack:
        while p != None:
            stack.append(p)
            p = p.left
        n = stack.pop()
        res.append(n.val)
        p = n.right
    return res

def preOrder(root):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def postOrder(root):
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        res.append(node.val)
    return res[::-1]


print(midOrder(node_dic[0]))
print(preOrder(node_dic[0]))
print(postOrder(node_dic[0]))