# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if int(math.log10(num) + 1) % 2 == 0)
