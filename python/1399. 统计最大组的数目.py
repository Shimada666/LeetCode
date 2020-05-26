# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n + 1):
            k = sum(map(int, str(i)))  # 以按位求和的和作为键
            d[k] = d.get(k, 0) + 1
        return sum([1 for k in d if d[k] == max(d.values())])
