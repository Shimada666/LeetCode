# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int((1 + len(nums)) * (len(nums) / 2) - sum(nums))


print(Solution().missingNumber([3,0,1]))
