# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        dic = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        tmp = sorted(nums, reverse=True)
        return [dic[tmp.index(x)] if tmp.index(x) in dic else str(tmp.index(x) + 1) for x in nums]