# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        res = 0
        for k, v in c.items():
            if k + 1 in c.keys():
                res = max(res, v + c[k + 1])
        return res
