# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        numerator = 1 #分子
        denominator = cont[-1] #分母
        for i in range(len(cont)-1,0,-1):
            numerator,denominator = denominator,numerator
            denominator = cont[i-1]*numerator+denominator
        return [denominator,numerator]
