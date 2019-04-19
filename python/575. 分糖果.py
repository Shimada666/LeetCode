# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)), len(candies) // 2)
