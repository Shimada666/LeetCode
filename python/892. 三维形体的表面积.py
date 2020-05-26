# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        a = 0
        ans = 0
        n = len(grid)
        for i in range(n):
            row = 0
            lie = 0
            for j in range(n):
                if grid[i][j] > 0:
                    a = a + 1
                ans = ans + abs(row - grid[i][j]) + abs(lie - grid[j][i])
                lie = grid[j][i]
                row = grid[i][j]
            ans = ans + row + lie
        return(ans+a*2)
