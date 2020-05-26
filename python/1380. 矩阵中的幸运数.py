# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mins = set(min(rows) for rows in matrix)
        maxes = set(max(columns) for columns in zip(*matrix))
        return list(mins & maxes)
