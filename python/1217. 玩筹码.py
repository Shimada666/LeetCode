# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even = 0
        for c in chips:
            if c%2==0:
                even+=1
        return min(even,len(chips)-even)