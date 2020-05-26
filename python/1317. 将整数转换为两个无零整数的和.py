# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        while(True):
            L = random.randint(1,n)
            R = n-L
            if '0' not in str(L) and '0' not in str(R):
                return [L,R]
