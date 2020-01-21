# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        for index, ch in enumerate(s):
            if c[ch] == 1:
                return index
        return -1
