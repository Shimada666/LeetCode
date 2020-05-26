# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if nums[i] == i:
                stack.append(i)
        if not stack:
            return -1
        return min(stack)
