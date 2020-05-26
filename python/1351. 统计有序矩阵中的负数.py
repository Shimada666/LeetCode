# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        i, j = 0, len(grid[0]) - 1

        while i < len(grid) and j >= 0:
            if grid[i][j] >= 0:
                i += 1
            else:
                total += len(grid) - i
                j -= 1
        return total
