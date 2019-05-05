# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = {}
        for i, v in enumerate(numbers, 1):
            if target - v in temp:
                return [temp[target - v], i]
            if not v in temp:
                temp[v] = i