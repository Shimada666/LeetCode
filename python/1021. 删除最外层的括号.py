# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        start_index = 0
        res = ''
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(S[i])
            else:
                stack.pop()
            if not stack:
                res += S[start_index + 1:i]
                start_index = i + 1
        return res