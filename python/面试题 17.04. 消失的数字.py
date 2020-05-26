# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int((1 + len(nums)) * (len(nums) / 2) - sum(nums))
