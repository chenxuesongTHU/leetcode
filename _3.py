#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _3  
@Time        :   2021/3/12 8:40 下午
@Author      :   Xuesong Chen
@Description :   无重复字符的最长子串
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        if len(s) == 0:
            return max_len
        longest_sub = s[0]
        max_len = 1
        for idx in range(1, len(s)):
            current_char = s[idx]
            if current_char not in longest_sub:
                longest_sub += current_char
                current_len = len(longest_sub)
                if current_len > max_len:
                    max_len = current_len
            else:
                repeat_char_idx = longest_sub.find(current_char)
                longest_sub = longest_sub[repeat_char_idx+1:]
                longest_sub += current_char
        return max_len

if __name__ == '__main__':
    solution = Solution()
    print(
        solution.lengthOfLongestSubstring('abcabcbb'),
        solution.lengthOfLongestSubstring('bbbbb'),
        solution.lengthOfLongestSubstring('nfpdmpi'),
        solution.lengthOfLongestSubstring(''),
        sep='\n',
    )