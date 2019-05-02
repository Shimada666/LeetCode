# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        col_len = len(matrix)
        row_len = len(matrix[0])
        if col_len == 1 or row_len == 1:
            return True
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True