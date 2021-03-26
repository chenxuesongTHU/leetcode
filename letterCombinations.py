#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   letterCombinations  
@Time        :   2021/3/26 4:04 下午
@Author      :   Xuesong Chen
@Description :   电话号码的字母组合  todo
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        def backtrack(idx):
            if idx == n:
                combinations.append(''.join(combination))
                return

            for c in phoneMap[digits[idx]]:
                combination.append(c)
                backtrack(idx+1)
                combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations



print(
    Solution().letterCombinations('23')
)