#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   quickSort  
@Time        :   2021/3/15 1:17 下午
@Author      :   Xuesong Chen
@Description :   
"""

# 快速排序函数
def quicksort(nums):
    if len(nums) <= 1:
        return nums

    # 左子数组
    less = []
    # 右子数组
    greater = []
    # 基准数
    base = nums.pop()

    # 对原数组进行划分
    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)

    # 递归调用
    return quicksort(less) + [base] + quicksort(greater)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
# quickSort(arr, 0, n - 1
arr = quicksort(arr)
print("排序后的数组:")
print(arr)