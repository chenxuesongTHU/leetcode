#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   mergeTwoLists  
@Time        :   2021/3/26 10:52 下午
@Author      :   Xuesong Chen
@Description :   
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution_:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        l1_val = l1.val
        l2_val = l2.val
        if l1_val > l2_val:
            l2, l1 = l1, l2
        pre_node = l1
        res = l1
        while l1:
            if l1.val <= l2.val:
                pre_node = l1
                l1 = l1.next
            else:
                pre_node.next = l2
                pre_node = l2
                tmp = l1
                l1 = l2.next
                l2 = tmp
        pre_node.next = l2
        return res

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


def create_node(_list):

    head = ListNode(_list[0])
    pre = head
    for v in _list[1:]:
        node = ListNode(v)
        pre.next = node
        pre = node
    return head

l1 = create_node([2])
l2 = create_node([1])

print(
    Solution().mergeTwoLists(l1, l2)
)
