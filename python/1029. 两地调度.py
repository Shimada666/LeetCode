# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = [cost+[cost[0]-cost[1]] for cost in costs]
        costs.sort(key=lambda x: x[2])
        costMin, N = 0, int(len(costs) / 2)
        for i in range(2 * N):
            if i < N: costMin += costs[i][0]
            else: costMin += costs[i][1]
        return costMin
