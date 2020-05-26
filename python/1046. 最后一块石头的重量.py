# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i];
        heapify(stones)
        while len(stones) > 0:
            y = -heappop(stones)
            if len(stones) == 0:
                return y
            x = -heappop(stones)
            if x != y:
                heappush(stones, x - y)
        return 0
