# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(len(x) for x in ''.join(map(str,nums)).split('0'))