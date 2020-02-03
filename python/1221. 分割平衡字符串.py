# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c, r = 0, 0
        for i in s:
            if i == 'R': c += 1
            if i == 'L': c -= 1
            if c == 0: r += 1
        return r
