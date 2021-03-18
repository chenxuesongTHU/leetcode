#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   input  
@Time        :   2021/3/16 2:50 下午
@Author      :   Xuesong Chen
@Description :   
"""
# str = input()
# _s = str.split(' ')
# print(_s)
import heapq

li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(li1)
print(
    heapq.nlargest(3, li1),
    heapq.nsmallest(3, li1)

)
