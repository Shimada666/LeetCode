# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [x for x in range(n - 1)]
        ans.append(-sum(ans))
        return ans
