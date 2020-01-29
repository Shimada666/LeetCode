# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return grid
        m = len(grid)
        n = len(grid[0])
        trow = []
        for row in grid:
            trow += row
        tk = len(trow)
        k = k % tk
        nrow = trow[tk - k:tk] + trow[0:tk - k]
        for i in range(m):
            for j in range(n):
                grid[i][j] = nrow[i * n + j]
        return grid


if __name__ == '__main__':
    print(Solution().shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 1))
