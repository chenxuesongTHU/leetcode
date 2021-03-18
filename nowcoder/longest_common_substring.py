#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   longest_common_substring  
@Time        :   2021/3/16 10:17 上午
@Author      :   Xuesong Chen
@Description :   TODO
"""
class Solution:
    def LCS(self , str1 , str2 ):
        n, m = len(str1), len(str2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        p = (0,0)
        for i in range(1,n+1):
            for j in range(1,m+1):

                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] > dp[p[0]][p[1]]:
                    p = (i, j)
                else:
                    pass
        return str1[p[0]-dp[p[0]][p[1]]:p[0]]

if __name__ == '__main__':
    print(
        Solution().LCS("1AB2345CD", "12345EF")
    )
