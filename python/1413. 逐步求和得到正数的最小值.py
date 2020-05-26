# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        from itertools import accumulate
        return max(1, 1 - min(accumulate(nums)))
