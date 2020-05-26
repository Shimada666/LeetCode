# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = dict()
        for x in arr:
            m[x] = m.get(x, 0) + 1
        ans = -1
        for (key, value) in m.items():
            if key == value:
                ans = max(ans, key)
        return ans
