#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   KthLargest  
@Time        :   2021/3/18 10:54 上午
@Author      :   Xuesong Chen
@Description :   设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
"""
# todo
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.que = nums
        heapq.heapify(self.que)

    def add(self, val: int) -> int:
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]


# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
val = 4
param_1 = obj.add(val)
print(param_1)