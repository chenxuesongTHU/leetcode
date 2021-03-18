#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _6_zgg
@Time        :   2021/3/17 10:49 下午
@Author      :   Xuesong Chen
@Description :   Todo
"""
class Solution:
    def convert(self, s: str, m: int) -> str:
        n = len(s)
        d = 2*m-2
        if m == 1:
            return s
        idx = 0
        res = ''
        while idx < n:
            res += s[idx]
            idx += d
        for idx in range(1, m-1):
            aa_idx = idx
            bb_idx = d - idx
            while aa_idx < n:
                res += s[aa_idx]
                aa_idx += d
                if bb_idx < n:
                    res += s[bb_idx]
                    bb_idx += d
        idx = m-1
        while idx < n:
            res += s[idx]
            idx += d

        return res

if __name__ == '__main__':
    print(
        Solution().convert('0', 1)
    )
