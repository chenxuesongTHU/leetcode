#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   KthLargest
@Time        :   2021/3/18 10:54 上午
@Author      :   Xuesong Chen
@Description :   最小堆
"""

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr, n):
    i = n//2
    while i >= 0:
        heapify(arr, n, i)
        i -= 1
    print(arr)


    i = n-1
    while i >= 0:
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        i -= 1

    return arr

print(
    heapSort([32,12,2,4,6,45], 6)
)
