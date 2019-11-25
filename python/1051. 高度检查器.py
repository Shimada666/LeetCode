# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        return len([i for i in list(map(lambda x, y: x - y, heights, sorted_heights)) if i != 0])
