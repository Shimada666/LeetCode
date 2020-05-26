# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(1, length):
            subMaxSum = max(nums[i] + nums[i - 1], nums[i])
            nums[i] = subMaxSum
        return max(nums)
