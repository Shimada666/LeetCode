# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        while len(nums)>0:
            result.append(nums.pop())
            if sum(result) > sum(nums):
                return result
