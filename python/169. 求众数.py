# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


if __name__ == '__main__':
    print(Solution().majorityElement([1,1,2]))