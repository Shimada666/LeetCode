# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        i = 0
        for letter in set(s):
            t = s.count(letter)
            if t % 2 == 0:
                count += t
            else:
                count += t - 1
                i = 1
        return count + 1 if i else count
