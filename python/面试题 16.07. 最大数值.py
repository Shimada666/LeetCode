# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def maximum(self, a: int, b: int) -> int:
        k = bin((a - b) & ((1 << 63) - 1))
        idx = ("0" * (64 - len(k)) + k)[2]
        return [a, b][int(idx)]
