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
for y in range(n//2+1, 0, -1):
    x = n-2*y
    tili = s*x + t*pow(y, 2)
    if tili > m:
        continue
    else:
        time = u*x + v*y
        print(time)
        break
        # if min_time == None:
        #     min_time = time
        # if time < min_time:
        #     min_time = time
        # print(x, y, time, tili)

# print(min_time)