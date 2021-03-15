#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   lruDesign_cxs  
@Time        :   2021/3/15 3:25 下午
@Author      :   Xuesong Chen
@Description :   
"""

class Solution:
    def LRU(self , operators , k ):
        # write code here
        record_cache = {}
        freq_list = [] # key
        res = []
        for o in operators:
            if o[0] == 1:
                record_cache[o[1]] = o[2]
                freq_list.append(o[1])
                if len(freq_list) > k:
                    del record_cache[freq_list[0]]
                    del freq_list[0]

            if o[0] == 2:
                if o[1] in freq_list:
                    res.append(record_cache[o[1]])
                    freq_list.remove(o[1])
                    freq_list.append(o[1])
                else:
                    res.append(-1)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(
        solution.LRU([[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3)
    )
