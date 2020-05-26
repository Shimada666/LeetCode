# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans,x,y = [],1,1000
        while x <= z and y >= 1:
            res = customfunction.f(x,y)
            if res < z:
                x += 1
            elif res > z:
                y -= 1
            if res == z:
                ans.append([x,y])
                x += 1
                y -= 1
        return ans
