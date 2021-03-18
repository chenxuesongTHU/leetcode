#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _5  
@Time        :   2021/3/17 8:04 下午
@Author      :   Xuesong Chen
@Description :   最长的回文子串 TODO

"""
from pprint import pprint as print

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for i in range(n):
            dp[i][i] = True
        longest_s = 0
        longest_e = 0
        for end_i in range(1, n):
            for start_i in range(0, end_i):
                if s[start_i] == s[end_i] and end_i-start_i == 1:
                    dp[start_i][end_i] = True
                    if end_i - start_i > (longest_e - longest_s):
                        longest_s = start_i
                        longest_e = end_i
                else:
                    if s[start_i] == s[end_i] and dp[start_i+1][end_i-1] == True:
                        dp[start_i][end_i] = True
                        if end_i-start_i > (longest_e - longest_s):
                            longest_s = start_i
                            longest_e = end_i
        # print(dp)
        ans = s[longest_s:longest_e+1]
        return ans

if __name__ == '__main__':
    print(
        Solution().longestPalindrome('ac')
    )