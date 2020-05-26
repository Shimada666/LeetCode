# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        xy = sum([sum([1 if j else 0 for j in i]) for i in grid])  # m*n
        xz = sum([max(i) for i in grid])  # m*1
        yz = sum([max([grid[i][j] for i in range(m)]) for j in range(n)])  # n*1
        return xy + xz + yz
