# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        init_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if abs(three_sum - target) < abs(init_sum - target):
                    init_sum = three_sum
                if three_sum > target:
                    r -= 1
                elif three_sum < target:
                    l += 1
                else:
                    return target
        return init_sum

if __name__ == '__main__':
    print(Solution().threeSumClosest([-1, 2, 1, 4], 1))
