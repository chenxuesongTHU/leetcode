#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _20  
@Time        :   2021/3/17 11:23 下午
@Author      :   Xuesong Chen
@Description :   
"""

_map = {
    '}': '{',
    ']': '[',
    ')': '(',
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for _c in s:
            if _c in ['{', '[', '(']:
                stack.append(_c)
            else:
                if len(stack) != 0:
                    if _map[_c] == stack.pop():
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    print(
        Solution().isValid('{}')
    )
