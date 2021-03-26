#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   test_2  
@Time        :   2021/3/21 8:59 下午
@Author      :   Xuesong Chen
@Description :   
"""
n, u, v, s, t, m = map(int,input().split(' '))

min_time = None
for y in range(0, n//2+1):
    x = n-2*y
    tili = s*x + t*pow(y, 2)
    if tili > m:
        continue
    time = u*x + v*y
    if min_time == None:
        min_time = time
    if time < min_time:
        min_time = time
        # print(x, y, time, tili)

print(min_time)