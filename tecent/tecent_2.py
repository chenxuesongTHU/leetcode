#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   tecent_1  
@Time        :   2021/3/21 7:59 下午
@Author      :   Xuesong Chen
@Description :   
"""
# n=int(input())
# m=int(input())
n,m = map(int,input().split(' '))
f_1=list(map(int, input().split(' ')))
f_2=list(map(int, input().split(' ')))

t = 0
for _v in f_1:
    if _v in f_2:
        print(_v)
        t+=_v
    else:
        pass
print(t)


