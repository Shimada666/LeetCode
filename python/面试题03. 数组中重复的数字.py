# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
import collections


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for k, v in c.items():
            if v != 1:
                return k
