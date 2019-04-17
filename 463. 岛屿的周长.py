# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        sum_ = 0
        for i in grid:
            sum_ += sum(i)
        sum_ *= 4
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cnt = 0
                if grid[i][j] == 1:
                    if len(grid[i])>1:
                        if j - 1 < 0:
                            cnt += grid[i][j + 1]
                        elif j + 1 > len(grid[i]) - 1:
                            cnt += grid[i][j - 1]
                        else:
                            cnt += grid[i][j - 1] + grid[i][j + 1]

                    if len(grid) > 1:
                        if i - 1 < 0:
                            cnt += grid[i + 1][j]
                        elif i + 1 > len(grid) - 1:
                            cnt += grid[i - 1][j]
                        else:
                            cnt += grid[i - 1][j] + grid[i + 1][j]
                sum_ -= cnt
        return sum_


if __name__ == '__main__':
    print(Solution().islandPerimeter(
        [[0,1,0,0]]))
