#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   longestValidParentheses  
@Time        :   2021/3/16 10:44 上午
@Author      :   Xuesong Chen
@Description :   TODO
"""
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def longestValidParentheses(self , s ):
        # write code here
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ')':
                pre = i - dp[i - 1] - 1
                if pre >= 0 and s[pre] == '(':
                    dp[i] = dp[i - 1] + 2
                    if pre - 1 >= 0:
                        dp[i] += dp[pre - 1]
        if len(dp) > 0:
            return max(dp)
        return len(dp)

if __name__ == '__main__':
    print(
        Solution().longestValidParentheses('(())()')
    )