# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            print(6)
            s[i: i + k] = s[i: i + k][::-1]
        return ''.join(s)


s = "abcdefg"
print(Solution().reverseStr(s,2))