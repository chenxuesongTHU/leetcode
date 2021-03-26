#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   tecent_1  
@Time        :   2021/3/21 7:59 下午
@Author      :   Xuesong Chen
@Description :   
"""

# n=int(input())
# if n > 1:
#     f=list(map(int, input().split(' ')))
# else:
#     f=[int(input())]
n = 4
# f = [0, 20, 50, 60]
f = [0, 20, 50, 1000]

idx = 0

def get_cost(val):
    if val < 100:
        return 50
    elif 100 <= val < 1000:
        return 100
    else:
        return 20

cur_cost = 0
# total_time = 0
for _val in f:
    idx += 1
    count = idx
    # 第一种方式
    # total_time += _val
    if _val < 1000:
        cost_1 = count * 20
        cost_2 = get_cost(_val)
        new_cost = min(cost_1, cost_2)
        print(new_cost - cur_cost)
    else:
        cost_2 = get_cost(_val)

    cur_cost = new_cost
    # idx += 1