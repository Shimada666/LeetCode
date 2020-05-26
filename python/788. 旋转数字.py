# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans, d = 0, [0, 0, 1, -1, -1, 1, 1, -1, 0, 1] + [0] * (N - 9)
        for i in range(N + 1):
            d[i] = -1 in (d[i // 10], d[i % 10]) and -1 or d[i // 10] | d[i % 10]
            ans += d[i] == 1
        return ans
