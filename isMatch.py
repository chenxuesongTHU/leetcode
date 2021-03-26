#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   isMatch  
@Time        :   2021/3/25 10:46 上午
@Author      :   Xuesong Chen
@Description :   正则表达式匹配 todo
"""


# from pprint import pprint as print

class Solution_my:
    def isMatch(self, s: str, p: str) -> bool:
        n_row = len(p)
        n_col = len(s)
        dp = [[False] * (n_col + 1) for _ in range(n_row + 1)]
        dp[0][0] = True
        # print('\t', '\t'.join(s))

        # 初始化，需要考虑*的情况。即 'a*'能匹配上''的问题
        for p_idx in range(1, n_row+1):
            if p[p_idx-1] == '*':
                dp[p_idx][0] = dp[p_idx-2][0]

        for p_idx in range(1, n_row+1):
            for s_idx in range(1, n_col+1):
                # 最后一位相同，看前一位
                if p[p_idx-1] == s[s_idx-1] or '.' == p[p_idx-1]:
                    dp[p_idx][s_idx] = dp[p_idx-1][s_idx-1]
                if p[p_idx-1] == '*':
                    # *表示0个字母
                    if dp[p_idx-2][s_idx]:
                        dp[p_idx][s_idx] = dp[p_idx-2][s_idx]
                    else:
                    # *表示1个或多个字母 aaa a*
                        if p[p_idx-2] == s[s_idx-1] or p[p_idx-2] == '.':
                            dp[p_idx][s_idx] = dp[p_idx][s_idx-1] | dp[p_idx-2][s_idx-1]
        # print(dp)
        return dp[n_row][n_col]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        # dp[i][j] 表示 s[:i] 与 p[:j] 是否匹配，各自前 i、j 个是否匹配
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True

        # s 为空串
        for j in range(1, p_len + 1):
            # 若 p 的第 j 个字符 p[j - 1] 是 '*'
            # 说明第 j - 1、j 位可有可无
            # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                    # print(i, j, dp[i][j])
                elif p[j - 1] == '*':
                    if p[j - 2] in {s[i - 1], '.'}:
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
        print(dp)
        return dp[s_len][p_len]


print(
    'MY:',
    Solution_my().isMatch(
        "aa",
        ".*"
    ),
    '\n',
    'GT:',
    Solution().isMatch(
        "aaa", "a*"
    )
)

'''
        a a
    a
    *
'''
