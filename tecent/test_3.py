#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   test_3
@Time        :   2021/3/21 9:29 下午
@Author      :   Xuesong Chen
@Description :
"""
def jiecheng(v):
    ret = 1
    for i in range(1, v+1):
        ret *= i
    return ret

def not_start_0(z_n, n):
    if z_n == 0:
        return 0
    total = 0
    for n_zero in range(1, z_n+1):
        total += (n-z_n) * jiecheng(n-n_zero-1)
    return total

def continue_jiecheng(_list):
    res = 1
    for _v in _list:
        res *= jiecheng(_v)
    return res
# print(jiecheng(3))
from collections import Counter
n=int(input())
a=list(map(int, input().split(' ')))
c = dict(Counter(a))
m = len(c)
if 0 in c.keys():
    n_zero = c[0]
    # del c[0]
else:
    n_zero = 0
repet_list = c.values()
# print(c[0])
total = jiecheng(n)
buchongfu = total /
hefa = total - not_start_0(n_zero, n)
print(
    int(hefa/continue_jiecheng(repet_list))
)
